# 搜狗微信搜索 MCP 服务器

本项目提供了一个通过搜狗微信搜索文章的工具，并将其封装为一个 MCP (Model Context Protocol) 服务器。

**核心亮点：**

*   **微信文章搜索**：通过搜狗微信平台，实现对微信公众号文章的搜索。
*   **灵活查询**：支持通过关键词进行搜索，并可指定返回文章的数量。
*   **结构化输出**：返回的文章信息包含标题、摘要、URL、来源和日期等结构化数据，方便后续处理。
*   **MCP 服务器集成**：将微信文章搜索功能封装为 MCP 工具，方便其他 AI 代理或系统通过 MCP 协议调用。

## 如何使用

### 1. 环境准备

确保您的系统安装了 Python 3.10 或更高版本。

推荐使用 `uv` 进行依赖管理：

```bash
# 安装 uv (如果尚未安装)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 进入项目目录
cd sogou-weixin-mcp-server

# 使用 uv 安装依赖
uv sync
```

### 2. 作为 MCP 服务器使用

您可以将本项目作为 MCP 服务器运行，以便其他 AI 代理或系统通过 MCP 协议调用 `search_wechat_articles` 工具。

```bash
uv run server.py
```

服务器启动后，它将监听 MCP 客户端的请求。

### 3. Claude MCP 服务器配置示例

以下是一个 `mcp_server.json` 配置文件示例，用于将此 MCP 服务器连接到 Claude：

```json
{
  "mcp_servers": [
    {
      "name": "sogou-wechat-search",
      "type": "stdio",
      "command": ["uv", "--directory", "/space/sogou-weixin-mcp-server/", "run", "server.py"],
      "tools": [
        {
          "name": "search_wechat_articles",
          "description": "使用Miku_spider通过搜狗微信搜索文章。",
          "input_schema": {
            "type": "object",
            "properties": {
              "query": {
                "type": "string",
                "description": "搜索关键词。"
              },
              "top_num": {
                "type": "integer",
                "description": "返回文章的最大数量，默认为18篇。",
                "default": 18
              }
            },
            "required": ["query"]
          }
        }
      ]
    }
  ]
}