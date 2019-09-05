# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)
# 项目信息
project (Demo)
# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_SRCS 变量
aux_source_directory(. DIR_SRCS)
# 添加 math 子目录
add_subdirectory(math)

#编译选项
OPTION(BUILD_UNIT_TESTS        "tests"      OFF)

if(BUILD_UNIT_TESTS)
	add_subdirectory(tests)
endif()

# 指定生成目标 
add_executable(Demo main.c)
# 添加链接库
target_link_libraries(Demo MathFunctions)


install (TARGETS Demo DESTINATION ${PROJECT_BINARY_DIR}/bin)