#!/bin/bash
# ============================================
# 蓝鹰AI网关 - cURL 对话补全示例
# BlueEagle AI Gateway - cURL Chat Completion
#
# 官方网站: https://ahg.codes
# ============================================

# 请替换为你的API Key
API_KEY="YOUR_API_KEY"
BASE_URL="https://ahg.codes/v1"

echo "=== 蓝鹰AI网关 - 对话补全示例 ==="
echo ""

# GPT-4o 对话示例
echo ">>> GPT-4o 对话:"
curl -s "${BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${API_KEY}" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "system", "content": "你是一个专业、友好的AI助手。"},
      {"role": "user", "content": "你好，请用一句话介绍你自己"}
    ],
    "temperature": 0.7,
    "max_tokens": 1024
  }' | python3 -m json.tool 2>/dev/null || echo "请安装 python3 或 jq 来格式化输出"

echo ""
echo ">>> Claude 4 Sonnet 对话:"
curl -s "${BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${API_KEY}" \
  -d '{
    "model": "claude-4-sonnet",
    "messages": [
      {"role": "user", "content": "What is the meaning of life?"}
    ],
    "temperature": 0.7,
    "max_tokens": 1024
  }' | python3 -m json.tool 2>/dev/null || echo "请安装 python3 或 jq 来格式化输出"

echo ""
echo ">>> Gemini 2.5 Pro 对话:"
curl -s "${BASE_URL}/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${API_KEY}" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [
      {"role": "user", "content": "介绍一下量子计算的基本原理"}
    ],
    "temperature": 0.7,
    "max_tokens": 1024
  }' | python3 -m json.tool 2>/dev/null || echo "请安装 python3 或 jq 来格式化输出"
