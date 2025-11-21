from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime
import os

app = FastAPI(
    title="Crawl4AI API",
    description="Crawl4AI API",
    version="1.0.0"
)

# 安全验证器
security = HTTPBearer()

# API Key（从环境变量读取，默认值仅用于演示）
API_KEY = os.getenv("API_KEY", "api-key-here")

async def verify_api_key(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    验证API Key的依赖函数
    
    使用方式：在请求头中添加 Authorization: Bearer <your-api-key>
    """
    if credentials.credentials != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="无效的API Key",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials


@app.get("/check", dependencies=[Depends(verify_api_key)])
async def check():
    """健康检查接口（需要鉴权）"""
    return {
        "status": "ok",
        "message": "服务运行正常",
        "timestamp": datetime.now().isoformat()
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

