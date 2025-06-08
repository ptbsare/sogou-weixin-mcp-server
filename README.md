# Sogou WeChat Search MCP Server
[简体中文 README](README_CN.md)

This project provides a tool for searching articles through Sogou WeChat and encapsulates it as an MCP (Model Context Protocol) server.

**Key Highlights:**

*   **WeChat Article Search**: Enables searching for WeChat official account articles through the Sogou WeChat platform.
*   **Flexible Query**: Supports searching by keywords and specifying the number of articles to return.
*   **Structured Output**: Returns structured article information including title, snippet, URL, source, and date, facilitating further processing.
*   **MCP Server Integration**: Encapsulates the WeChat article search functionality as an MCP tool, allowing other AI agents or systems to call it via the MCP protocol.

## How to Use

### 1. Environment Setup

Ensure your system has Python 3.10 or higher installed.

It is recommended to use `uv` for dependency management:

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Navigate to the project directory
cd sogou-weixin-mcp-server

# Install dependencies using uv
uv sync
```

### 2. Usage as an MCP Server

You can run this project as an MCP server, allowing other AI agents or systems to call the `search_wechat_articles` tool via the MCP protocol.

```bash
uv run server.py
```

Once the server starts, it will listen for MCP client requests.

### 3. Claude MCP Server Configuration Example

Below is an example `mcp_server.json` configuration file to connect this MCP server to Claude:

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