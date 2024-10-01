from __future__ import annotations

from typing import Any

import aiosqlite
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    SystemMessage,
    trim_messages,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.sqlite.aio import AsyncSqliteSaver
from langgraph.graph import START, MessagesState, StateGraph
from langgraph.graph.graph import RunnableConfig
from langgraph.graph.state import CompiledStateGraph
from nonebot import logger
from typing_extensions import Self

from nonebot_plugin_nonechat.utils.parsers import MarkdownOutputParser

from ..config import plugin_config
from .constants import DATABASE_URL


class ChatLLM:
    _instance = None

    def __new__(cls, *args, **keyargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, 'initialized'):
            # 设置模型
            self.llm: ChatOpenAI = ChatOpenAI(
                model=plugin_config.nonechat_model,
                api_key=plugin_config.nonechat_api_key,
                base_url=plugin_config.nonechat_base_url,
                temperature=plugin_config.nonechat_temperature,
                timeout=plugin_config.nonechat_timeout,
            )
            # 创建graph
            self.builder = StateGraph(MessagesState)
            self.builder.add_edge(START, 'model')
            self.builder.add_node('model', self.call_model)
            self.initialized: bool = True

    async def call_model(self, state: MessagesState) -> dict[str, BaseMessage]:
        max_tokens = plugin_config.nonechat_max_tokens
        # 使用预设
        prompt: ChatPromptTemplate = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=plugin_config.nonechat_prompt),
                MessagesPlaceholder(variable_name='messages'),
            ],
        )
        # 如果max_tokens > 0时，对input message进行裁剪
        if max_tokens > 0:
            trimmer = trim_messages(
                strategy='last',
                token_counter=len,
                max_tokens=max_tokens,
                start_on='human',
                end_on=('human', 'tool'),
                include_system=True,
            )
            chain = prompt | trimmer | self.llm
        else:
            chain = prompt | self.llm
        response = await chain.ainvoke(dict(state))
        return {'messages': response}

    async def chat(self, id: str, content: str) -> str:
        """对话功能

        Args:
            id (str): 用户/群组id
            content (str): 用户输入的内容

        Returns:
            str: llm生成的输出
        """
        async with aiosqlite.connect(DATABASE_URL) as conn:
            graph: CompiledStateGraph = self.builder.compile(AsyncSqliteSaver(conn))
            config: RunnableConfig = RunnableConfig(configurable={'thread_id': id})
            input_messages: list[HumanMessage] = [
                HumanMessage(f'{content}，请使用markdown格式输出')
                if plugin_config.nonechat_output_format == 'markdown'
                else HumanMessage(content)
            ]
            output: dict[str, Any] | Any = await graph.ainvoke(
                {'messages': input_messages}, config
            )
            logger.debug(output)
            output_message: str = output['messages'][-1].content
            # 按照设置的过滤词过滤回复
            if any(
                word in output_message for word in plugin_config.nonechat_filter_words
            ):
                return '该回复已被过滤'
            else:
                # 如果设置了输出格式为markdown，则对消息进行解析后返回
                if plugin_config.nonechat_output_format == 'markdown':
                    return MarkdownOutputParser().parser(output_message)
                else:
                    return output_message
