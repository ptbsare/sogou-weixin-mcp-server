# Sogou WeChat Search MCP Server
[简体中文 README](README_CN.md)

This project provides a tool for searching articles through Sogou WeChat and encapsulates it as an MCP (Model Context Protocol) server.

**Key Highlights:**

*   **WeChat Article Search**: Enables searching for WeChat official account articles through the Sogou WeChat platform.
*   **Flexible Query**: Supports searching by keywords and specifying the number of articles to return.
*   **Structured Output**: Returns structured article information including title, snippet, URL, source, and date, facilitating further processing.
*   **MCP Server Integration**: Encapsulates the WeChat article search functionality as an MCP tool, allowing other AI agents or systems to call it via the MCP protocol.

## How to Use

### Quick Start (Recommended)

You can run the server directly with `uvx` — no clone, no install, no setup:

```bash
uvx --from git+https://github.com/ptbsare/sogou-weixin-mcp-server.git sogou-weixin-mcp-server
```

This downloads and runs the latest version in one shot.

### 1. Environment Setup (Local Development)

Ensure your system has Python 3.10 or higher installed.

It is recommended to use `uv` for dependency management:

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone the repository
git clone https://github.com/ptbsare/sogou-weixin-mcp-server.git
cd sogou-weixin-mcp-server

# Install dependencies using uv
uv sync
```

### 2. Usage as an MCP Server

You can run this project as an MCP server, allowing other AI agents or systems to call the `search_wechat_articles` tool via the MCP protocol.

```bash
# Run via uv (local directory)
uv run sogou-weixin-mcp-server

# Or run the script directly
uv run server.py
```

Once the server starts, it will listen for MCP client requests over stdio.

### 3. Claude MCP Server Configuration Example

Below is an example `mcp_server.json` configuration file to connect this MCP server to Claude:

#### Option A: Using uvx (no local clone needed)

```json
{
  "mcp_servers": [
    {
      "name": "sogou-wechat-search",
      "type": "stdio",
      "command": ["uvx", "--from", "git+https://github.com/ptbsare/sogou-weixin-mcp-server.git", "sogou-weixin-mcp-server"]
    }
  ]
}
```

#### Option B: Using local directory

```json
{
  "mcp_servers": [
    {
      "name": "sogou-wechat-search",
      "type": "stdio",
      "command": ["uv", "--directory", "/path/to/sogou-weixin-mcp-server/", "run", "server.py"]
    }
  ]
}
```

### 4. Available Tools

#### `search_wechat_articles`

Search for WeChat articles via Sogou WeChat.

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `query` | string | Yes | — | Search keyword |
| `top_num` | integer | No | 18 | Maximum number of articles to return |

**Returns:** A list of dictionaries, each containing:
- `title` — Article title
- `snippet` — Article summary/snippet
- `url` — Article URL
- `source` — WeChat official account name
- `date` — Publication date
