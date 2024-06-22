# job的设计

## web服务管理shell脚本
- 启动时候，会自动加载指定目录的shell脚本，并形成swagger文档
- 系统支持通用参数
  - HTTP method: 缺省是POST，除非shell文件以'get'开头，则为get请求
  - _async: 异步执行，缺省是false，同步执行
  - _timeout: 脚本执行超时时间，单位是秒，缺省是60秒
  - _env: 脚本执行时候的环境变量，格式是json字符串，缺省是空
  - HTTP headers: 
    - Authorization: Bearer 用户token 调用方使用的token
- 收到http请求后，会根据请求的路径，找到对应的shell脚本，并执行
- 程序会设置env环境变量，shell脚本运行时候可以获取这些env变量
  - HTTP_REQUEST_METHOD
  - HTTP_REQUEST_URI
  - HTTP_REQUEST_QUERY
  - HTTP_REQUEST_BODY
  - HTTP_REQUEST_ID 自动分配的请求id
- 如果是异步执行
  - 返回 HTTP_REQEST_ID给到http请求
- 脚本执行过程中的输出，会自动写入logs/{HTTP_REQUEST_ID}.log文件
- 脚本需要返回的json内容，要自行写入logs/{HTTP_REQUEST_ID}.response.json文件
- 脚本执行完毕后，会返回结果给http请求
  - 读取logs/{HTTP_REQUEST_ID}.response.json文件，返回给http请求
  - 如果脚本执行成功，会返回200状态码给http请求
  - 如果脚本执行失败，会返回500状态码给http请求
  - 如果脚本执行超时，会返回504状态码给http请求
- 返回如下的json格式给调用方
  ```json
  {
    "code": 200,
    "message": "success",
    "data": {
      "result": "success"
    }
  }
  ```

