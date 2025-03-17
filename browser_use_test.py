# from browser_use import Browser as BrowserUseBrowser
from app.tool.browser_use_tool import BrowserUseTool
import asyncio



async def browserTest():
    # 初始化浏览器
    browserUseTool = BrowserUseTool()
    await browserUseTool.execute(action = "navigate",url= "https://www.baidu.com")
    # res = await browserUseTool.execute(action = "screenshot",url= "https://www.baidu.com")
    res = await browserUseTool.execute(action = "read_links",url= "https://www.baidu.com")
    print(res.output)
    print(res.system)

# if __name__ == "__main__":
#     browserTest()

if __name__ == "__main__":
    asyncio.run(browserTest())