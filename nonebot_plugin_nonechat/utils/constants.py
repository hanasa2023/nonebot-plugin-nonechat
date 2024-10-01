from nonebot import require

require('nonebot_plugin_localstore')
from nonebot_plugin_localstore import get_data_file

DATABASE_URL = get_data_file(
    plugin_name='nonebot-plugin-nonechat', filename='memory.db'
)
