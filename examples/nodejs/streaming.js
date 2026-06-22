/**
 * 蓝鹰AI网关 - Node.js 流式输出示例
 * BlueEagle AI Gateway - Node.js Streaming Example
 *
 * 官方网站: https://ahg.codes
 */

import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: 'YOUR_API_KEY',
  baseURL: 'https://ahg.codes/v1',
});

async function streamChat(model = 'gpt-4o', prompt = '用中文写一首关于蓝鹰的诗') {
  try {
    console.log(`模型: ${model}`);
    console.log(`问题: ${prompt}`);
    console.log('-'.repeat(50));
    process.stdout.write('回复: ');

    const stream = await client.chat.completions.create({
      model,
      messages: [
        { role: 'system', content: '你是一个有创意的AI助手。' },
        { role: 'user', content: prompt },
      ],
      stream: true,
      temperature: 0.8,
      max_tokens: 2048,
    });

    let fullResponse = '';

    for await (const chunk of stream) {
      const content = chunk.choices[0]?.delta?.content;
      if (content) {
        process.stdout.write(content);
        fullResponse += content;
      }
    }

    console.log('\n' + '-'.repeat(50));
    console.log(`完整回复长度: ${fullResponse.length} 字符`);
  } catch (error) {
    console.error('请求失败:', error.message);
  }
}

// 执行示例
(async () => {
  await streamChat('gpt-4o');
  console.log('\n');
  await streamChat('claude-4-sonnet', 'Explain quantum computing in simple terms');
})();
