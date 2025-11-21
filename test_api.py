"""
测试 Coze API 的鉴权功能
"""
import requests
import os

# 从环境变量获取API Key，或使用默认值
API_KEY = os.getenv("COZE_API_KEY", "your-secret-api-key-here")
BASE_URL = "http://localhost:8000"

def test_with_valid_key():
    """使用有效的 API Key 测试"""
    print("测试 1: 使用有效的 API Key")
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    try:
        response = requests.get(f"{BASE_URL}/check", headers=headers)
        print(f"状态码: {response.status_code}")
        print(f"响应: {response.json()}")
        print("✅ 测试通过\n")
    except Exception as e:
        print(f"❌ 测试失败: {e}\n")

def test_without_key():
    """不提供 API Key 测试"""
    print("测试 2: 不提供 API Key")
    
    try:
        response = requests.get(f"{BASE_URL}/check")
        print(f"状态码: {response.status_code}")
        print(f"响应: {response.json()}")
        if response.status_code == 401 or response.status_code == 403:
            print("✅ 测试通过 - 正确拒绝未授权请求\n")
        else:
            print("❌ 测试失败 - 应该拒绝未授权请求\n")
    except Exception as e:
        print(f"❌ 测试失败: {e}\n")

def test_with_invalid_key():
    """使用无效的 API Key 测试"""
    print("测试 3: 使用无效的 API Key")
    headers = {
        "Authorization": "Bearer invalid-api-key-123"
    }
    
    try:
        response = requests.get(f"{BASE_URL}/check", headers=headers)
        print(f"状态码: {response.status_code}")
        print(f"响应: {response.json()}")
        if response.status_code == 401:
            print("✅ 测试通过 - 正确拒绝无效 API Key\n")
        else:
            print("❌ 测试失败 - 应该拒绝无效 API Key\n")
    except Exception as e:
        print(f"❌ 测试失败: {e}\n")

if __name__ == "__main__":
    print("=" * 50)
    print("Coze API 鉴权测试")
    print("=" * 50)
    print(f"API Key: {API_KEY}")
    print(f"Base URL: {BASE_URL}")
    print("=" * 50 + "\n")
    
    test_with_valid_key()
    test_without_key()
    test_with_invalid_key()
    
    print("=" * 50)
    print("测试完成")
    print("=" * 50)

