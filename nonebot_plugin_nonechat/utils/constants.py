from pathlib import Path

from nonebot import require

require('nonebot_plugin_localstore')
from nonebot_plugin_localstore import get_plugin_data_dir

DATABASE_URL: Path = get_plugin_data_dir() / 'db' / 'memory.db'
