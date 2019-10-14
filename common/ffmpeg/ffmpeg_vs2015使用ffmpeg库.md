

## 1，目标

搭建windows下 ffmpeg的开发环境

## 2，需要的文件

去官方下载ffmpeg  可参见：http://ffmpeg.zeranoe.com/builds/  

包含三个版本：Static、Shared以及Dev

- Static   包含3个应用程序：ffmpeg.exe , ffplay.exe , ffprobe.exe，体积都很大，相关的DLL已经被编译到exe里面去了。


- Shared  除了ffmpeg.exe , ffplay.exe , ffprobe.exe之外还有一些DLL，exe体积很小，在运行时到相应的DLL中调用功能。


- Dev      开发者（developer）版本，里面包含了库文件xxx.lib以及头文件xxx.h，这个版本不含exe文件
  

我们使用的是来自Shared版本的dll文件，和来自Dev的include目录下的头文件和lib文件。



## 3，demo

### cmake配置文件

```cmake
# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)
# 项目信息
project (Demo)
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
#aux_source_directory(. DIR_SRCS)
# 添加 math 子目录
#add_subdirectory(math)




if(NOT LIBFFMPEG_FOUND)
	set(LIBFFMPEG_INCLUDE_DIRS ${PROJECT_SOURCE_DIR}/3rdparty/ffmpeg/inc)
  
	set(LIBFFMPEG_PATH "${PROJECT_SOURCE_DIR}/3rdparty/ffmpeg/lib")
    set(LIBFFMPEG_NAME  "avcodec.lib")
    #set(LIBFFMPEG_NAME  "libavcodec.lib  libavdevice.lib  libavformat libavutil libavfilter")
  #set(LIBSOFTFILTER_BIN_PATH "${ROOT_SOURCE_DIR}/3rdparty/libMX6500/libs" )
endif()

message(${LIBFFMPEG_INCLUDE_DIRS})

include_directories(${LIBFFMPEG_INCLUDE_DIRS} 
					)
link_directories( ${LIBFFMPEG_PATH} )

# 指定生成目标 
add_executable(Demo FFmpegTest.cpp)
# 添加链接库
target_link_libraries(Demo  ${LIBFFMPEG_NAME} avdevice.lib avfilter.lib avformat.lib avutil.lib)


install (TARGETS Demo DESTINATION ${PROJECT_BINARY_DIR}/bin)

# 构建一个 CPack 安装包
include (InstallRequiredSystemLibraries)

#set (CPACK_RESOURCE_FILE_LICENSE  "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set (CPACK_PACKAGE_VERSION_MAJOR "${Demo_VERSION_MAJOR}")
set (CPACK_PACKAGE_VERSION_MINOR "${Demo_VERSION_MINOR}")
include (CPack)
```

### 测试源码

FFmpegTest.cpp 中的代码内容使用sample中的metadata.c 作为测试代码





## 4，报错及解决

### error LNK2026: 模块对于 SAFESEH 映像是不安全的

#### 解决方法1

1.打开该项目的“属性页”对话框。

2.单击“链接器”文件夹。

3.单击“命令行”属性页。

4.将 /SAFESEH:NO 键入“其他选项”框中，然后点击应用。

#### 解决方法2

在cmake中增加设置

```cmake
#模块对于SAFESEH映像是不安全
set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} /SAFESEH:NO")
set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} /SAFESEH:NO")
set(CMAKE_MODULE_LINKER_FLAGS "${CMAKE_MODULE_LINKER_FLAGS} /SAFESEH:NO")
```



### 运行时报错：

```
无法定位程序输入点av_file_map 于动态链接库。。。上
```

原因可能是使用的lib文件与实际的不匹配



## 5，参考链接

1. [ffmpeg官网](http://ffmpeg.org/)
2. [FFmpeg专栏 | 代码导读——基础篇(一) ](http://www.livevideostack.com/portal.php?mod=view&aid=65)
3. [FFmpeg编译指南](https://trac.ffmpeg.org/wiki/CompilationGuide)

