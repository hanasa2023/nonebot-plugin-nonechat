from nonebot import on_message, require
from nonebot.adapters import Event
from nonebot.rule import to_me

from .config import plugin_config
from .utils.llm import ChatLLM

require('nonebot_plugin_alconna')
require('nonebot_plugin_htmlrender')
from nonebot_plugin_alconna import UniMessage
from nonebot_plugin_htmlrender import md_to_pic

chat = on_message(rule=to_me())


@chat.handle()
async def _(event: Event):
    # 获取用户输入消息
    input: str = event.get_plaintext()
    # 过滤输入的消息
    if any(word in input for word in plugin_config.nonechat_filter_words):
        await chat.finish('此消息含有违禁词，已被自动过滤')
    llm = ChatLLM()
    id: str = str(UniMessage.get_target(event).id)
    output = await llm.chat(id, input)
    if plugin_config.nonechat_output_format == 'markdown':
        img: bytes = await md_to_pic(md=output)
        await UniMessage().image(raw=img).send(event)
        await chat.finish()
    else:
        await chat.finish(output)
