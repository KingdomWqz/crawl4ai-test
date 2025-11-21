# Coze FastAPI 应用

一个简单的 FastAPI 应用，提供基础的健康检查接口。所有接口都需要通过 API Key 鉴权。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置 API Key

应用使用环境变量来配置 API Key。你可以通过以下方式设置：

```bash
export COZE_API_KEY="your-secret-api-key"
```

如果不设置环境变量，默认使用 `your-secret-api-key-here` 作为 API Key（仅用于开发测试）。

**⚠️ 生产环境请务必设置强密钥！**

## 运行应用

```bash
# 设置 API Key 后运行
export COZE_API_KEY="your-secret-api-key"
python main.py
```

或者使用 uvicorn 命令：

```bash
export COZE_API_KEY="your-secret-api-key"
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API 鉴权

所有 API 接口都需要在请求头中携带 Bearer Token：

```bash
Authorization: Bearer <your-api-key>
```

### 示例请求

使用 curl：

```bash
curl -X GET "http://localhost:8000/check" \
  -H "Authorization: Bearer your-secret-api-key"
```

使用 Python requests：

```python
import requests

headers = {
    "Authorization": "Bearer your-secret-api-key"
}

response = requests.get("http://localhost:8000/check", headers=headers)
print(response.json())
```

使用 JavaScript fetch：

```javascript
fetch('http://localhost:8000/check', {
  headers: {
    'Authorization': 'Bearer your-secret-api-key'
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

## API 接口

### GET /check
- 描述：健康检查接口
- 鉴权：需要 Bearer Token
- 响应：
```json
{
    "status": "ok",
    "message": "服务运行正常",
    "timestamp": "2025-11-21T10:30:00.123456"
}
```

### 鉴权失败响应

如果 API Key 无效或未提供，会返回 401 错误：

```json
{
    "detail": "无效的API Key"
}
```

## API 文档

启动应用后，可以访问以下地址查看自动生成的 API 文档：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

**注意**：在 Swagger UI 中使用接口时，需要先点击右上角的 "Authorize" 按钮，输入你的 API Key。

## 测试鉴权

项目提供了一个测试脚本来验证鉴权功能：

```bash
# 确保服务正在运行
python main.py

# 在另一个终端运行测试
python test_api.py
```

测试脚本会执行以下三个测试：
1. ✅ 使用有效的 API Key - 应该成功
2. ✅ 不提供 API Key - 应该返回 401 错误
3. ✅ 使用无效的 API Key - 应该返回 401 错误

