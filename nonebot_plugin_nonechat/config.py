from __future__ import annotations

from typing import Any

from nonebot import get_plugin_config
from pydantic import BaseModel, SecretStr, validator


class Config(BaseModel):
    """Plugin Config Here"""

    # 使用的模型
    nonechat_model: str = 'glm-4-flash'
    # 相应的api_key
    nonechat_api_key: SecretStr = SecretStr('')
    # api接口地址
    nonechat_base_url: str = 'https://open.bigmodel.cn/api/paas/v4/'
    # 使用的预设
    nonechat_prompt: str = ''
    # 过滤词
    nonechat_filter_words: list[str] = []
    # 单次消息的最大token数
    nonechat_max_tokens: int = 0
    # 采样温度
    nonechat_temperature: float = 0.5
    # 响应超时时间
    nonechat_timeout: float = 60
    # 输出格式
    nonechat_output_format: str = ''
    # http(s)代理
    nonechat_proxy: tuple[str, str] | None = None

    @validator('nonechat_proxy', pre=True)
    def parse_proxy(cls, v) -> tuple[str, str] | Any:
        if isinstance(v, str):
            host, port = v.split(',')
            return host, port
        return v


plugin_config: Config = get_plugin_config(Config)
