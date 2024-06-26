""" 主程序文件 """
from fastapi import FastAPI
# from .routers import items, users

app = FastAPI()

# app.include_router(items.router)
# app.include_router(users.router)

@app.get("/")
def read_root():
    """ 返回一个简单的JSON """
    return {"Hello": "World"}

@app.get("/status")
def read_status():
    """ 检查服务状态 """
    return {"status": "ok"}

# 运行应用程序
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # 监听所有网络接口的8000端口
