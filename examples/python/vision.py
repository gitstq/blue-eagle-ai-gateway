"""
蓝鹰AI网关 - Python 图像识别示例（Vision）
BlueEagle AI Gateway - Python Vision Example

官方网站: https://ahg.codes
"""

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://ahg.codes/v1"
)

def analyze_image(image_url: str, prompt: str = "请详细描述这张图片的内容"):
    """使用GPT-4o分析图片"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                            "detail": "high"  # 可选: "low", "high", "auto"
                        }
                    }
                ]
            }
        ],
        max_tokens=2048
    )

    print(f"图片分析结果:")
    print(response.choices[0].message.content)
    return response


def analyze_image_base64(image_path: str, prompt: str = "描述这张图片"):
    """使用Base64编码的图片进行分析"""

    import base64

    with open(image_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}"
                        }
                    }
                ]
            }
        ],
        max_tokens=2048
    )

    print(f"图片分析结果:")
    print(response.choices[0].message.content)
    return response


if __name__ == "__main__":
    # 使用URL分析图片
    analyze_image(
        image_url="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg",
        prompt="请用中文详细描述这张图片中的内容"
    )

    # 使用本地图片分析（取消注释并替换路径）
    # analyze_image_base64("path/to/your/image.jpg", "描述这张图片")
