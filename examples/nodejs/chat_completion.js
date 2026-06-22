/**
 * 蓝鹰AI网关 - Node.js 对话补全示例
 * BlueEagle AI Gateway - Node.js Chat Completion Example
 *
 * 官方网站: https://ahg.codes
 */

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',           // 替换为你的蓝鹰API Key
  baseURL: 'https://ahg.codes/v1',   // 蓝鹰API地址
});

async function chatCompletion(model = 'gpt-4o', message = '你好，蓝鹰！') {
  try {
    const response = await client.chat.completions.create({
      model,
      messages: [
        { role: 'system', content: '你是一个专业、友好的AI助手。' },
        { role: 'user', content: message },
      ],
      temperature: 0.7,
      max_tokens: 2048,
    });

    console.log(`模型: ${model}`);
    console.log(`回复: ${response.choices[0].message.content}`);
    console.log(
      `Token使用 - 输入: ${response.usage.prompt_tokens}, ` +
      `输出: ${response.usage.completion_tokens}, ` +
      `总计: ${response.usage.total_tokens}`
    );

    return response;
  } catch (error) {
    console.error('请求失败:', error.message);
  }
}

async function multiTurnChat() {
  const messages = [
    { role: 'system', content: '你是一个专业的编程助手。' },
  ];

  console.log('=== 多轮对话模式 ===\n');

  // 模拟多轮对话
  const userMessages = [
    '什么是蓝鹰AI网关？',
    '它有什么核心优势？',
    '如何快速开始使用？',
  ];

  for (const userMsg of userMessages) {
    console.log(`用户: ${userMsg}`);
    messages.push({ role: 'user', content: userMsg });

    const response = await client.chat.completions.create({
      model: 'gpt-4o',
      messages,
      temperature: 0.7,
      max_tokens: 1024,
    });

    const assistantReply = response.choices[0].message.content;
    messages.push({ role: 'assistant', content: assistantReply });
    console.log(`AI: ${assistantReply}\n`);
  }
}

// 执行示例
(async () => {
  await chatCompletion('gpt-4o', '用一句话介绍蓝鹰AI网关的核心优势');
  console.log('\n' + '='.repeat(50) + '\n');
  await multiTurnChat();
})();
