<div align="center">

# 🦅 蓝鹰AI网关 | BlueEagle AI Gateway

### 🌍 全球顶尖大模型统一API网关 — 一站式接入所有主流AI模型
### The Unified API Gateway for All Leading AI Models

**⚡ 0.09x 极致倍率 | 💰 1:1 充值比例 | 🔒 100% 原生官方号池 | 🔄 零代码迁移**

[![0.09x Ultra Low Rate](https://img.shields.io/badge/倍率-0.09x-blue?style=for-the-badge&labelColor=black)](https://ahg.codes)
[![1:1 Recharge](https://img.shields.io/badge/充值-1%3A1-green?style=for-the-badge&labelColor=black)](https://ahg.codes)
[![100% Official Pool](https://img.shields.io/badge/号池-100%25原生官方-orange?style=for-the-badge&labelColor=black)](https://ahg.codes)
[![OpenAI Compatible](https://img.shields.io/badge/接口-OpenAI兼容-9cf?style=for-the-badge&labelColor=black)](https://ahg.codes)
[![Free Trial](https://img.shields.io/badge/测试-免费额度-success?style=for-the-badge&labelColor=black)](https://ahg.codes)
[![Pay As You Go](https://img.shields.io/badge/计费-按量付费-yellow?style=for-the-badge&labelColor=black)](https://ahg.codes)

**🌐 官方网站：[https://ahg.codes](https://ahg.codes)**

[快速开始](#-快速开始--quick-start) · [支持模型](#-支持模型--supported-models) · [充值说明](#-充值与计费--pricing) · [竞品对比](#-竞品对比--comparison) · [联系我们](#-联系与支持--contact)

</div>

---

## 📖 项目简介 | About

**蓝鹰AI网关（BlueEagle AI Gateway）** 是一个面向全球开发者和企业的高质量AI大模型API中转服务。通过统一的标准OpenAI兼容接口，用户可以一站式接入 OpenAI GPT、Anthropic Claude、Google Gemini、Antigravity 等全球顶尖大模型，享受极致性价比的AI调用体验。

> **核心亮点**：充值比例 **1:1**（充1元=1美元官方额度），消耗倍率仅 **0.09x**（仅为官方定价的 **9%**），相当于用不到一折的价格使用全球顶级AI模型。

**BlueEagle AI Gateway** is a premium AI model API relay service for global developers and enterprises. Through a unified OpenAI-compatible interface, users can access OpenAI GPT, Anthropic Claude, Google Gemini, Antigravity and other world-leading AI models with ultimate cost efficiency.

> **Key Highlight**: 1:1 recharge ratio (1 CNY = 1 USD official credit), only 0.09x consumption rate (just **9%** of official pricing) — use the world's top AI models at less than 10% of the cost.

---

## ✨ 核心优势 | Core Advantages

| 优势 Advantage | 详情 Details |
|---|---|
| 💰 **0.09x 极致倍率** | 仅为官方定价的9%，GPT-4o每百万Token仅需约$0.72 |
| 💵 **1:1 充值比例** | 充1元人民币 = 1美元官方额度，无汇率损耗 |
| 🔒 **100% 原生官方号池** | 无掺假、无共享、无二次中转，纯净原生通道 |
| 🎁 **免费测试额度** | 注册即送测试额度，零成本体验全部模型 |
| ⚡ **毫秒级故障切换** | 多账号智能负载均衡，自动检测并切换故障节点 |
| 🔌 **零代码迁移** | 完全兼容OpenAI接口规范，仅需修改 `base_url` |
| ♾️ **额度永久有效** | 按量计费，用多少付多少，余额永不过期 |
| 🌐 **全球加速节点** | 多区域部署，低延迟高可用 |

---

## 📋 支持模型 | Supported Models

| 模型系列 Model Series | 支持模型 Supported Models | 状态 Status |
|---|---|---|
| **OpenAI GPT** | GPT-4o, GPT-4o-mini, GPT-4-Turbo, GPT-4, GPT-3.5-Turbo, o1, o1-mini, o3, o3-mini, DALL·E 3 | ✅ 已支持 |
| **Anthropic Claude** | Claude 4 Opus, Claude 4 Sonnet, Claude 3.5 Sonnet, Claude 3.5 Haiku, Claude 3 Opus, Claude 3 Sonnet | ✅ 已支持 |
| **Google Gemini** | Gemini 2.5 Pro, Gemini 2.5 Flash, Gemini 2.0 Flash, Gemini 1.5 Pro, Gemini 1.5 Flash | ✅ 已支持 |
| **Antigravity** | Antigravity 全系列 | ✅ 已支持 |
| **DeepSeek** | DeepSeek V3, DeepSeek R1 | 🔜 即将支持 |
| **通义千问 Qwen** | Qwen-Max, Qwen-Plus | 🔜 即将支持 |
| **Meta Llama** | Llama 3, Llama 3.1 | 🔜 即将支持 |

> 📌 持续更新中，更多模型即将上线！模型名称与官方完全一致，直接替换 `base_url` 即可使用。

---

## 🚀 快速开始 | Quick Start

### 方式一：cURL（最快速）

```bash
curl https://ahg.codes/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {"role": "user", "content": "Hello, BlueEagle!"}
    ],
    "max_tokens": 1024
  }'
```

### 方式二：Python（推荐）

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://ahg.codes/v1"
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, BlueEagle!"}
    ],
    max_tokens=1024
)

print(response.choices[0].message.content)
```

### 方式三：Node.js

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://ahg.codes/v1'
});

const response = await client.chat.completions.create({
  model: 'gpt-4o',
  messages: [
    { role: 'system', content: 'You are a helpful assistant.' },
    { role: 'user', content: 'Hello, BlueEagle!' }
  ],
  max_tokens: 1024
});

console.log(response.choices[0].message.content);
```

### 方式四：流式输出（Streaming）

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://ahg.codes/v1"
)

stream = client.chat.completions.create(
    model="claude-4-sonnet",
    messages=[{"role": "user", "content": "写一首关于蓝鹰的诗"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
```

> 💡 **迁移指南**：如果你已经在使用 OpenAI SDK，只需将 `base_url` 改为 `https://ahg.codes/v1`，`api_key` 改为蓝鹰的 API Key，其余代码 **无需任何修改**！

---

## 💰 充值与计费 | Pricing

### 计费公式 | Billing Formula

```
实际扣费 = 官方Token单价 × 0.09 × Token消耗量
```

### 充值示例 | Recharge Examples

| 充值金额 Recharge | 获得额度 Credits | 相当于官方价值 Official Equivalent | 节省 Savings |
|---|---|---|---|
| ¥10 CNY | $10 USD | ~$111 USD | **节省 91%** |
| ¥50 CNY | $50 USD | ~$556 USD | **节省 91%** |
| ¥100 CNY | $100 USD | ~$1,111 USD | **节省 91%** |
| ¥500 CNY | $500 USD | ~$5,556 USD | **节省 91%** |

### 使用示例 | Usage Example

以 **GPT-4o** 为例（官方定价：输入 $2.5/百万Token，输出 $10/百万Token）：

| 操作 Operation | 官方费用 Official Cost | 蓝鹰费用 BlueEagle Cost |
|---|---|---|
| 输入 100万 Token | $2.50 | **$0.225** |
| 输出 100万 Token | $10.00 | **$0.90** |
| 日常对话 1000次 (~500K Token) | ~$3.75 | **~$0.34** |

> 💡 额度永久有效，按量扣费，用多少扣多少，零浪费！

---

## ⚔️ 竞品对比 | Comparison

| 对比维度 Dimension | **蓝鹰AI网关 BlueEagle** | 官方直连 Official | 其他中转站 Other Relays |
|---|:---:|:---:|:---:|
| **消耗倍率 Rate** | **0.09x** ✅ | 1.0x | 0.3x ~ 1.5x |
| **充值比例 Recharge** | **1:1** ✅ | 1:7.2 | 1:5 ~ 1:10 |
| **号池质量 Pool Quality** | **100% 原生官方** ✅ | 官方 | 混合/不确定 |
| **故障切换 Failover** | **毫秒级自动** ✅ | 无 | 部分支持 |
| **免费测试 Free Trial** | **✅ 注册即送** | ❌ | 部分支持 |
| **接口兼容 Compatibility** | **OpenAI 100%** ✅ | OpenAI | 部分兼容 |
| **额度有效期 Validity** | **永久有效** ✅ | 按月 | 30天~永久 |
| **支持模型数量 Models** | **50+** ✅ | 各家独立 | 10~30 |
| **负载均衡 Load Balance** | **多账号智能** ✅ | 无 | 部分支持 |

---

## 📁 项目结构 | Project Structure

```
blue-eagle-ai-gateway/
├── README.md                    # 项目主页（本文件）
├── LICENSE                      # MIT 开源协议
├── examples/
│   ├── python/
│   │   ├── chat_completion.py   # Python 对话补全示例
│   │   ├── streaming.py         # Python 流式输出示例
│   │   └── vision.py            # Python 图像识别示例
│   ├── nodejs/
│   │   ├── chat_completion.js   # Node.js 对话补全示例
│   │   └── streaming.js         # Node.js 流式输出示例
│   └── curl/
│       ├── chat_completion.sh   # cURL 对话补全示例
│       └── models_list.sh       # cURL 模型列表查询
└── docs/
    └── migration_guide.md        # 从其他平台迁移指南
```

---

## 🔗 更多资源 | Resources

- 🌐 **官方网站**：[https://ahg.codes](https://ahg.codes)
- 📖 **API文档**：[https://ahg.codes/docs](https://ahg.codes/docs)
- 🔑 **获取API Key**：[https://ahg.codes/register](https://ahg.codes/register)
- 💬 **技术支持**：[https://ahg.codes/support](https://ahg.codes/support)

---

## 📞 联系与支持 | Contact & Support

如有任何问题或建议，欢迎通过以下方式联系我们：

- 🌐 访问官网提交工单：[https://ahg.codes](https://ahg.codes)
- 📧 邮件联系：support@ahg.codes
- 💬 在线客服：官网右下角即时聊天

---

## ⚠️ 免责声明 | Disclaimer

本项目（GitHub仓库）仅为 **蓝鹰AI网关** 的使用说明和示例代码仓库，旨在帮助开发者快速接入和使用蓝鹰AI网关服务。

- 本仓库中的示例代码基于 OpenAI SDK 开源协议发布
- 蓝鹰AI网关服务由其运营团队独立运营，本仓库不承担任何服务相关责任
- 使用本服务时，请遵守相关AI模型的使用条款和当地法律法规
- 价格和模型支持情况可能随时调整，请以官网 [https://ahg.codes](https://ahg.codes) 最新信息为准

---

<div align="center">

**⭐ 如果蓝鹰AI网关对你有帮助，请给这个仓库一个 Star！**

**If BlueEagle AI Gateway helps you, please give this repo a Star! ⭐**

Made with 🦅 by BlueEagle Team | [https://ahg.codes](https://ahg.codes)

</div>
