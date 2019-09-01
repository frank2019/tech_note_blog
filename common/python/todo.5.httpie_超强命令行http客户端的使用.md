

# 概述



HTTPie 是一个 HTTP 的命令行客户端，目标是让 CLI 和 web 服务之间的交互尽可能的人性化。这个工具提供了简洁的 http 
命令，允许通过自然的语法发送任意 HTTP 请求数据，展示色彩化的输出。HTTPie 可用于与 HTTP 服务器做测试、调试和常规交互。

## **主要特性：**

- 直观的语法
- 格式化和色彩化的终端输出
- 内置 JSON 支持
- 支持上传表单和文件
- HTTPS、代理和认证
- 任意请求数据
- 自定义头部
- 持久性会话
- 类 Wget 下载
- 支持 Python 2.6, 2.7 和 3.x
- 支持 Linux, Mac OS X 和 Windows
- 插件
- 文档
- 测试覆盖率

HTTPie 是用 Python 编写，用到了 [Requests](http://python-requests.org/) 和 [Pygments](http://pygments.org/) 这些出色的库。

**Github**：https://github.com/jakubroztocil/httpie

# 使用

## 安装

windows平台

```
easy_install  httpie
```

验证安装成功

```
http  baidu.com
HTTP/1.1 200 OK
Accept-Ranges: bytes
Cache-Control: max-age=86400
Connection: Keep-Alive
Content-Length: 81
Content-Type: text/html
Date: Sun, 30 Jun 2019 14:17:49 GMT
ETag: "51-47cf7e6ee8400"
Expires: Mon, 01 Jul 2019 14:17:49 GMT
Last-Modified: Tue, 12 Jan 2010 13:48:00 GMT
Server: Apache

<html>
<meta http-equiv="refresh" content="0;url=http://www.baidu.com/">
</html>
```



## 命令

```
http
usage: http [--json] [--form] [--pretty {all,colors,format,none}]
            [--style STYLE] [--print WHAT] [--headers] [--body] [--verbose]
            [--all] [--history-print WHAT] [--stream] [--output FILE]
            [--download] [--continue]
            [--session SESSION_NAME_OR_PATH | --session-read-only SESSION_NAME_OR_PATH]
            [--auth USER[:PASS]] [--auth-type {basic,digest}]
            [--proxy PROTOCOL:PROXY_URL] [--follow]
            [--max-redirects MAX_REDIRECTS] [--timeout SECONDS]
            [--check-status] [--verify VERIFY]
            [--ssl {ssl2.3,ssl3,tls1,tls1.1,tls1.2}] [--cert CERT]
            [--cert-key CERT_KEY] [--ignore-stdin] [--help] [--version]
            [--traceback] [--default-scheme DEFAULT_SCHEME] [--debug]
            [METHOD] URL [REQUEST_ITEM [REQUEST_ITEM ...]]
```

## 示例



# 参考链接

1. [官网](https://httpie.org/)
2. https://www.cnblogs.com/new_2050/p/7745788.html

