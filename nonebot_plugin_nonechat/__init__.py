from nonebot.plugin import PluginMetadata, inherit_supported_adapters

from .chat import chat
from .config import Config

__version__ = '0.1.2'
__plugin_meta__ = PluginMetadata(
    name='nonechat',
    description='大语言模型的简单接入',
    usage='对接OpenAI、chatglm等大语言模型',
    type='application',
    homepage='https://github.com/hanasa2023/nonebot-plugin-nonechat#readme',
    config=Config,
    supported_adapters=inherit_supported_adapters('nonebot_plugin_alconna'),
    extra={
        'version': __version__,
        'authors': [
            'hanasaki <hanasakayui2022@gmail.com>',
        ],
    },
)
