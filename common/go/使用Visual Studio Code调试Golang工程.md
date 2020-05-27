# 关键字

- 最简单的调试攻略
- 多项目调试, 适用个人开发和项目开发
- 无需修改系统环境变量

## 准备VSCode

在官网下载最新版的VSCode:

[Visual Studio Code - Code Editing. Redefined**](http://link.zhihu.com/?target=https%3A//code.visualstudio.com/)

## 安装Golang插件

- 打开扩展面板

  VSCode->查看->扩展

- 找到Go插件 在搜索框里输入Go, 找到第二行写有 Rich Go language support for Visual Studio Code的插件, 点击安装

  注意不是排名最高的

- 重启编辑器

## 配置启动项

- 打开调试面板

  VSCode->查看->调试

- 添加调试目标

  在"没有调试"的下拉框中点击"添加配置.."

- 添加目标调试配置

  例子:

  ```
  {
      "version": "0.2.0",
      "configurations": [
          {
              "name": "Launch",
              "type": "go",
              "request": "launch",
              "mode": "debug",
              "remotePath": "",
              "port": 2345,
              "host": "127.0.0.1",
              "program": "${fileDirname}",
              "env": {
                  "GOPATH":"D:/Develop/vscodegolang"
              },
              "args": [],
              "showLog": true
          }
      ]
  }

  ```

其中: "port", "host"都是go插件自动生成的

"env"为设置环境变量, 设置为你的工程目录就可以(包含bin, src的文件夹)

## 准备调试插件

此时找到main.go按F5, 会报错提示:

```
Failded to continue:"Cannot find Delve debugger. Install from https://github.com/derekparker/delve & ensure it is in your "GOPATH/bin" or "PATH"

```

我们使用go命令行编译调试器

```
go get github.com/derekparker/delve/cmd/dlv

```

将dlv调试器放在GOPATH(工程目录)的bin目录下

## 开始调试

选中要调试的main.go, 点击F5, 既可以开始调试

调试快捷键和Visual Studio系一致

- F9 切换断点
- F10 Step over
- F11 Step in
- Shift+F11 Step out

注意点

- 某些结构体成员无法直接显示时, 可以直接选中变量名, 添加到监视, 或者右键点击: "调试:求值"

## 多项目调试

在launch.json中可以添加多组调试入口, 通过调试面板中选中对应的配置开启不同目标的调试

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "client",
            "type": "go",
            "request": "launch",
            "mode": "debug",
            "remotePath": "",
            "port": 2345,
            "host": "127.0.0.1",
            "program": "${fileDirname}",
            "env": {
                "GOPATH":"D:/Develop/vscodegolang"
            },
            "args": [],
            "showLog": true
        },

        {
            "name": "server",
            "type": "go",
            "request": "launch",
            "mode": "debug",
            "remotePath": "",
            "port": 2345,
            "host": "127.0.0.1",
            "program": "${workspaceRoot}/src/server",
            "env": {
                "GOPATH":"D:/Develop/vscodegolang"
            },
            "args": [],
            "showLog": true
        }
    ]
}

```

"program"中的"${fileDirname}"是以当前选中文件作为启动点

更建议使用"program"的"${workspaceRoot}", 以包名作为启动点的方式进行配置

## 参考链接

[Debugging in Visual Studio Code](http://link.zhihu.com/?target=https%3A//code.visualstudio.com/Docs/editor/debugging)