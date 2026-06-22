# 从其他平台迁移到蓝鹰AI网关指南
# Migration Guide to BlueEagle AI Gateway

## 通用迁移步骤 | General Migration Steps

无论你当前使用的是哪个平台，迁移到蓝鹰AI网关只需 **3 步**：

### Step 1: 注册并获取 API Key

访问 [https://ahg.codes](https://ahg.codes) 注册账号，在控制面板中创建 API Key。

### Step 2: 修改配置

只需修改两个参数：

| 参数 Parameter | 原值 Original | 新值 New Value |
|---|---|---|
| `base_url` / `baseURL` | 原平台的API地址 | `https://ahg.codes/v1` |
| `api_key` / `apiKey` | 原平台的Key | 蓝鹰的API Key |

### Step 3: 测试验证

发送一个简单的请求验证连接是否正常：

```bash
curl https://ahg.codes/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_BLUEEAGLE_KEY" \
  -d '{"model":"gpt-4o","messages":[{"role":"user","content":"Hello!"}]}'
```

---

## 从 OpenAI 官方迁移

```python
# 修改前 - OpenAI 官方
client = OpenAI(api_key="sk-xxx")

# 修改后 - 蓝鹰AI网关
client = OpenAI(
    api_key="YOUR_BLUEEAGLE_KEY",
    base_url="https://ahg.codes/v1"
)
```

---

## 从其他中转站迁移

```python
# 修改前 - 其他中转站
client = OpenAI(
    api_key="sk-xxx",
    base_url="https://other-relay.com/v1"
)

# 修改后 - 蓝鹰AI网关
client = OpenAI(
    api_key="YOUR_BLUEEAGLE_KEY",
    base_url="https://ahg.codes/v1"
)
```

---

## Node.js 迁移

```javascript
// 修改前
const client = new OpenAI({ apiKey: 'sk-xxx' });

// 修改后
const client = new OpenAI({
  apiKey: 'YOUR_BLUEEAGLE_KEY',
  baseURL: 'https://ahg.codes/v1'
});
```

---

## 环境变量配置（推荐）

```bash
# .env 文件
OPENAI_API_KEY=YOUR_BLUEEAGLE_KEY
OPENAI_BASE_URL=https://ahg.codes/v1
```

使用环境变量后，大多数支持 OpenAI SDK 的框架和工具（如 LangChain、LlamaIndex、Dify 等）将自动适配，无需修改任何代码。

---

## 常见问题 | FAQ

**Q: 模型名称是否需要修改？**
A: 不需要。蓝鹰AI网关使用与官方完全一致的模型名称，如 `gpt-4o`、`claude-4-sonnet`、`gemini-2.5-pro` 等。

**Q: 流式输出是否支持？**
A: 完全支持，与官方SDK的流式接口完全一致。

**Q: 原有代码需要修改吗？**
A: 只需修改 `base_url` 和 `api_key`，其余代码无需任何修改。

**Q: 支持哪些SDK？**
A: 支持所有兼容OpenAI接口规范的SDK，包括官方Python/Node.js SDK、LangChain、LlamaIndex等。
