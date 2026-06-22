"""
蓝鹰AI网关 - Python 流式输出示例
BlueEagle AI Gateway - Python Streaming Example

官方网站: https://ahg.codes
"""

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://ahg.codes/v1"
)

def stream_chat(model: str = "gpt-4o", prompt: str = "用中文写一首关于蓝鹰的诗"):
    """流式输出对话"""

    print(f"模型: {model}")
    print(f"问题: {prompt}")
    print("-" * 50)
    print("回复: ", end="", flush=True)

    stream = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一个有创意的AI助手。"},
            {"role": "user", "content": prompt}
        ],
        stream=True,
        temperature=0.8,
        max_tokens=2048
    )

    full_response = ""
    for chunk in stream:
        if chunk.choices and chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            print(content, end="", flush=True)
            full_response += content

    print("\n" + "-" * 50)
    print(f"完整回复长度: {len(full_response)} 字符")


if __name__ == "__main__":
    # GPT-4o 流式输出
    stream_chat(model="gpt-4o")

    print("\n")

    # Claude 流式输出
    stream_chat(model="claude-4-sonnet", prompt="Explain quantum computing in simple terms")
