"""
蓝鹰AI网关 - Python 对话补全示例
BlueEagle AI Gateway - Python Chat Completion Example

官方网站: https://ahg.codes
API文档: https://ahg.codes/docs
"""

from openai import OpenAI

# 初始化客户端 - 只需修改 base_url 和 api_key
# Initialize client - just change base_url and api_key
client = OpenAI(
    api_key="YOUR_API_KEY",           # 替换为你的蓝鹰API Key
    base_url="https://ahg.codes/v1"   # 蓝鹰API地址
)

def chat_completion(model: str = "gpt-4o", message: str = "你好，蓝鹰！"):
    """发送对话补全请求"""

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "你是一个专业、友好的AI助手。"},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        max_tokens=2048,
        top_p=1.0
    )

    # 输出结果
    print(f"模型: {model}")
    print(f"回复: {response.choices[0].message.content}")
    print(f"Token使用 - 输入: {response.usage.prompt_tokens}, "
          f"输出: {response.usage.completion_tokens}, "
          f"总计: {response.usage.total_tokens}")

    return response


def multi_turn_chat():
    """多轮对话示例"""
    messages = [
        {"role": "system", "content": "你是一个专业的编程助手。"}
    ]

    print("=== 多轮对话模式（输入 'quit' 退出）===\n")

    while True:
        user_input = input("你: ").strip()
        if user_input.lower() == "quit":
            print("对话结束。")
            break

        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
            max_tokens=2048
        )

        assistant_reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": assistant_reply})

        print(f"AI: {assistant_reply}\n")


if __name__ == "__main__":
    # 单次对话
    chat_completion(
        model="gpt-4o",
        message="用一句话介绍蓝鹰AI网关的核心优势"
    )

    print("\n" + "=" * 50 + "\n")

    # 多轮对话（取消注释以使用）
    # multi_turn_chat()
