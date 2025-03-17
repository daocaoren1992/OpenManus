import asyncio
from openai import AsyncOpenAI,AsyncAzureOpenAI



async def call_silicon(prompt: str, model: str = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", temperature: float = 0.7, max_tokens: int = 100):
    api_key = "sk-qflmzxfkpnbfftjclfrtzyrvaysspzfqopkzlnfrtuyiahjwdbca"
    base_url = "https://api.siliconflow.cn/v1"
    client = AsyncOpenAI(api_key=api_key, base_url=base_url)

    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": prompt}
    ]

    # 需要 await 调用 API
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        stream=False,
        timeout=30,
    )

    # 解析返回内容
    if not response.choices or not response.choices[0].message.content:
        raise ValueError("Empty or invalid response from LLM")

    return response.choices[0].message.content



if __name__ == "__main__":
    user_input = "你能干什么"

    # 使用 asyncio 运行异步方法
    response = asyncio.run(call_silicon(user_input))
    print("OpenAI 回复:", response)
