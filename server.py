import asyncio # 引入 asyncio 支持异步操作
from miku_ai import get_wexin_article
from mcp.server.fastmcp import FastMCP
# 创建一个FastMCP服务器实例
mcp = FastMCP("SougouWeChatSearchServer")

def clean_text(text: str) -> str:
    """清理单个字符串中的无效Unicode代理项，保留URL不变"""
    if not isinstance(text, str):
        return text
    
    # 如果看起来像URL，直接返回原值（避免破坏合法URL）
    if text.startswith(('http://', 'https://')):
        return text
    
    # 仅对非URL文本进行清理
    return text.encode('utf-8', 'ignore').decode('utf-8')

@mcp.tool()
async def search_wechat_articles(
	query: str,
	top_num: int = 18
) -> list[dict[str,str]]:
	"""
	使用Miku_spider通过搜狗微信搜索文章。
	
	Args:
		query: 搜索关键词。
		top_num: 返回文章的最大数量，默认为18篇。
		
	Returns:
		一个包含文章标题、摘要、URL、来源和日期的字典列表。
	"""

	try:
		articles = await get_wexin_article(query, top_num=top_num)
		
		if not articles:
			return []
		
		formatted_articles = []
		for article in articles:
			# 过滤掉空的URL（Miku_spider可能返回空URL的文章）
			if article.get("url"):
				formatted_articles.append({
					"title": clean_text(article.get("title", "无标题")),
					"snippet": clean_text(article.get("snippet", "无摘要")),
					"url": article.get("url"), 
					"source": clean_text(article.get("source", "未知来源")),
					"date": clean_text(article.get("date", "未知日期"))
				})
		
		return formatted_articles

	except Exception as e:
		# 返回一个空列表，以明确表示操作失败但不会崩溃
		return []

#async def main():
#	await mcp.run(transport="stdio")

#if __name__ == "__main__":
#	asyncio.run(main())
# 如果直接运行此脚本，则启动MCP服务器
if __name__ == "__main__":
	# 默认使用STDIO传输协议，方便本地调试
	mcp.run(transport="stdio")

