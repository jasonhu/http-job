# http-job的配置文件

## 配置项
- PORT 监听端口，默认是8000
- JOBS_DIR shell文件所在目录，可以有多个，默认是./jobs
- TOKENS 用于验证的token，可以有多个值，如果为空，则不进行验证
- JOB_TIMEOUT 同步任务超时时间，单位是秒，默认是60
- JOB_ASYNC_TIMEOUT 异步任务超时时间，单位是秒，默认是300

## 配置文件格式

配置文件使用yaml格式，配置文件中可以包含多个job，每个job可以配置多个task，每个task可以配置多个task。

## 配置文件示例

```yaml
jobs:
  - name: job1
    tasks:
      - name: task1
        url: http://www.example.com
        method: GET
        headers: