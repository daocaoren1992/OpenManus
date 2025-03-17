import asyncio
from app.tool.search import WebSearchEngine, BaiduSearchEngine, GoogleSearchEngine, DuckDuckGoSearchEngine




async def searchTest():
    query = "日历"
    baidu = BaiduSearchEngine()
    res = baidu.perform_search(query)
    print(res)
    # google = GoogleSearchEngine()
    # res = google.perform_search(query)
    # print(res)
    duckDuckGo = DuckDuckGoSearchEngine()
    res = await  duckDuckGo.perform_search(query)
    print(res)

if __name__ == "__main__":
    asyncio.run(searchTest())