#!/bin/bash
# ============================================
# 蓝鹰AI网关 - cURL 模型列表查询
# BlueEagle AI Gateway - cURL List Models
#
# 官方网站: https://ahg.codes
# ============================================

API_KEY="YOUR_API_KEY"
BASE_URL="https://ahg.codes/v1"

echo "=== 蓝鹰AI网关 - 可用模型列表 ==="
echo ""

curl -s "${BASE_URL}/models" \
  -H "Authorization: Bearer ${API_KEY}" | python3 -m json.tool 2>/dev/null || \
  curl -s "${BASE_URL}/models" \
  -H "Authorization: Bearer ${API_KEY}"

echo ""
echo ""
echo "=== 查询单个模型信息 ==="
echo ""

curl -s "${BASE_URL}/models/gpt-4o" \
  -H "Authorization: Bearer ${API_KEY}" | python3 -m json.tool 2>/dev/null || \
  curl -s "${BASE_URL}/models/gpt-4o" \
  -H "Authorization: Bearer ${API_KEY}"
