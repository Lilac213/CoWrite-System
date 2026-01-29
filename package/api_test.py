
import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# 加载 .env
env_path = os.path.join(os.path.dirname(__file__), 'dist', '.env')
if not os.path.exists(env_path):
    print(f"❌ 找不到配置文件: {env_path}")
    sys.exit(1)

load_dotenv(env_path)

# 获取配置
api_key = os.getenv("POLISH_API_KEY")
base_url = os.getenv("POLISH_BASE_URL")
model = os.getenv("POLISH_MODEL")

print(f"配置文件路径: {env_path}")
print(f"API Key: {api_key[:10]}******" if api_key else "❌ 未设置 API Key")
print(f"Base URL: {base_url}")
print(f"Model: {model}")
print("-" * 50)

if not api_key or not base_url or not model:
    print("❌ 配置不完整，请检查 .env 文件")
    sys.exit(1)

client = OpenAI(api_key=api_key, base_url=base_url)

print("正在尝试连接 API...")
try:
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": "Hello, are you working?"}],
        max_tokens=20
    )
    print("✅ 连接成功！")
    print("🤖 AI 回复:", response.choices[0].message.content)
except Exception as e:
    print("❌ 连接失败！错误详情：")
    print(e)
    print("-" * 50)
    print("建议检查：")
    print("1. 网络连接 (是否需要代理？)")
    print("2. Base URL 是否正确 (结尾是否有 /v1 ?)")
    print("3. 模型名称是否正确 (gemini-2.0-flash 或 gemini-1.5-pro)")
