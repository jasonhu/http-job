# run job on http

## 介绍
- 使用python的fastapi框架开发
- 设计简单，使用http请求来触发任务
- 支持shell脚本和python脚本两种任务类型
- 支持多任务同时运行
- 支持同步任务和异步任务
- 支持异步任务状态和结果查询
- 支持token保护机制

## 运行
- 安装依赖
```
pip install -r requirements.txt
```
- 运行
```
python app/main.py
```

## 测试
- 测试接口
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "test", "script": "echo hello"}' http://127.0.0.1:8000/job
```
- 测试查询接口
```
curl http://127.0.0.1:8000/job/test
```

## 容器打包
- 打包
```
docker build -t http-job:0.1 .
```
- 运行
```
docker run -p 8000:8000 http-job:0.1
```

## 部署
- 运行容器
```
docker run -p 8000:8000 http-job:0.1
```
- 测试接口
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "test", "script": "echo hello"}' http://127.0.0.1:8000/job
```
- 测试查询接口
```
curl http://127.0.0.1:8000/job/test
```
