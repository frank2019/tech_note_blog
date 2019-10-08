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