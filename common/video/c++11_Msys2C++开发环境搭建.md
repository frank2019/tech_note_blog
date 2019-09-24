

## 目标

本文主要描述基于vscode 和Msys2 在windows下搭建c/c++开发环境



## 安装Msys2 及minGW

参看文件   [c++11_minGW64安装](c++11_minGW64安装.md)



## 配置VScode

### 安装vscode

下载安装 vscode ： https://code.visualstudio.com/

### **安装扩展**

- C/C++
   用于代码提示和补全
- Code Runner
   用于生成(build)并运行(run)

安装完成后须点击`重新加载`或重启VSCode



### **更改设置**

打开`用户设置`，setting.json 加入如下项

```json
	// 生成 build & 运行 run  若已使用 Code Runner，注意和已有设置的关系
    // Whether to run code in Integrated Terminal.
    "code-runner.runInTerminal": true,
    // Set the executor of each language.
    "code-runner.executorMap": {
        "c": "cd $dir && gcc $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
        "cpp": "cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt",
    },

    // Set the executor of each file extension.
    "code-runner.executorMapByFileExtension": {
    }
```

验证 Run code

- 在VSCode中打开一个文件夹，打开里面的一个源文件，
- `ctrl`+`shift`+`p`打开`命令面板`，运行其中的 `Run Code`，
- 该源文件将被编译生成目标文件，并在VSCode里的终端中运行
- 也可使用 Code Runner 的默认快捷键`ctrl`+`shift`+`n`，如果该快捷键之前没有被占用



```json
 // 调试 debug
    "launch": {
        "configurations": [
            {
                "name": "(gdb) Launch",
                "type": "cppdbg",
                "request": "launch",
                "program": "${workspaceFolder}/${fileBasenameNoExtension}",
                "args": [],
                "stopAtEntry": false,
                "cwd": "${workspaceFolder}",
                "environment": [],
                "externalConsole": true,
                "MIMode": "gdb",
                "miDebuggerPath": "gdb.exe",
                "setupCommands": [
                    {
                        "description": "Enable pretty-printing for gdb",
                        "text": "-enable-pretty-printing",
                        "ignoreFailures": true
                    }
                ]
            }
        ],
        "compounds": []
    },
```



现在，可以`f5`进行运行调试



## 参考链接

1. [VS Code 安装与配置（使用MSYS2环境与mingw-w64 编译环境）](https://blog.csdn.net/weixin_30908941/article/details/99217579)
2. [VSCode+MinGW(MSYS2) C++环境搭建](https://www.jianshu.com/p/65e20d4b3d58)

