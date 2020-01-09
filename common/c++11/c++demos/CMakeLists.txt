# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)
# 项目信息
project (Demo)
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)
# 添加 chrono 子目录
add_subdirectory(chrono)

#编译选项
OPTION(BUILD_UNIT_TESTS        "tests"      OFF)

if(BUILD_UNIT_TESTS)
	add_subdirectory(tests)
endif()

include_directories("${PROJECT_SOURCE_DIR}/chrono"  "${PROJECT_SOURCE_DIR}/common")


# 指定生成目标 
add_executable(Demo main.cpp)
# 添加链接库
target_link_libraries(Demo chrono)


# 指定生成目标 
add_executable(demo_enable_shared_from_this demo_enable_shared_from_this.cpp)







install (TARGETS Demo DESTINATION ${PROJECT_BINARY_DIR}/bin)

# 构建一个 CPack 安装包
include (InstallRequiredSystemLibraries)

#set (CPACK_RESOURCE_FILE_LICENSE  "${CMAKE_CURRENT_SOURCE_DIR}/License.txt")
set (CPACK_PACKAGE_VERSION_MAJOR "${Demo_VERSION_MAJOR}")
set (CPACK_PACKAGE_VERSION_MINOR "${Demo_VERSION_MINOR}")
include (CPack)