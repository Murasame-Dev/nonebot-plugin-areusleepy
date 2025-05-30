from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from . import __main__ as __main__
from . import getsleepy as getsleepy

from nonebot_plugin_apscheduler import scheduler
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="AreYouSleepy",
    description="基于 sleepy-project/sleepy 项目的状态查询插件！",
    usage="/areusleepy /getsleepy url",
    type="application",
    homepage="",
    supported_adapters=inherit_supported_adapters("nonebot_plugin_alconna"),
    config=Config,
)

config = get_plugin_config(Config)

