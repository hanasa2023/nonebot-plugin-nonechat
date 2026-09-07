<div align="center">

<a href="https://v2.nonebot.dev/store">
    <img src="./docs/NoneBotPlugin.svg" width="300" alt="logo">
</a>

# nonebot-plugin-nonechat

[![License](https://img.shields.io/github/license/hanasa2023/nonebot-plugin-nonechat.svg)](./LICENSE)
[![PyPI](https://img.shields.io/pypi/v/nonebot-plugin-nonechat.svg)](https://pypi.python.org/pypi/nonebot-plugin-nonechat)
![NoneBot](https://img.shields.io/badge/nonebot-2.3.0+-red.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)

</div>

## 📖 介绍

大语言模型的简单接入

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>

在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

```sh
    nb plugin install nonebot-plugin-nonechat
```

</details>

<details>
<summary>使用包管理器安装</summary>

在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

```sh
  pip install nonebot-plugin-nonechat
```

</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

```python
plugins = ['nonebot_plugin_nonechat']
```

</details>

## 🎉 使用

### 🚨 注意

- 目前只支持接入智谱清言的 glm 语言模型 ~~理论上支持 chatgpt，我没 token 没测过~~
- ~~http(s)代理设置理论有效~~
- glm 的 api key 请前往[glm api key](https://open.bigmodel.cn/usercenter/apikeys)获取

### 🔧 插件配置

请在你的 bot 根目录下的`.env` `.env.*`中添加以下字段

|         字段          |   类型    |                 默认值                  | 可选值 |                          描述                          | 必填 |
| :-------------------: | :-------: | :-------------------------------------: | :----: | :----------------------------------------------------: | :--: |
|    NONECHAT_MODEL     |    str    |              "glm-4-flash"              |   -    |                     插件使用的模型                     |  否  |
|   NONECHAT_API_KEY    |    str    |                    -                    |   -    |                      你的 api key                      |  是  |
|   NONECHAT_BASE_URL   |    str    | "https://open.bigmodel.cn/api/paas/v4/" |   -    |                 调用的 llm api 接入点                  |  否  |
|    NONECHAT_PROMPT    |    str    |                    -                    |   -    |                       使用的预设                       |  否  |
| NONECHAT_FILTER_WORDS | list[str] |                   []                    |   -    |             对用户输入及 ai 输出内容的过滤             |  否  |
|  NONECHAT_MAX_TOKENS  |    int    |                    0                    |   -    | 单次消息的最大 token 数，若为小于等于 0 的数则不做限制 |  否  |
| NONECHAT_TEMPERATURE  |   float   |                   0.5                   |   -    |                        采样温度                        |  否  |
|   NONECHAT_TIMEOUT    |   float   |                   60                    |   -    |                     响应的超时时间                     |  否  |
|    NONECHAT_PROXY     |    str    |                    -                    |   -    |       使用的 http(s)代理，格式为"{host}, {port}"       |  否  |

### ✨ 功能介绍

- [x] 在群聊里与接入的 LLM 进行对话（通过@直接进行对话）

### 🚩 TODO

- [x] 接入 openai 的 chatgpt 系列模型
- [ ] ai 绘图功能
- [ ] 获取生成的 markdown 图片的原始数据
- [ ] 多预设值的设置与选取
- [ ] 私聊支持
