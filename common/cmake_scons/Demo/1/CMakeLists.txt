# CMake 最低版本号要求
cmake_minimum_required (VERSION 2.8)
# 项目信息
project (Demo1)
# 显示指定使用的C++编译器 
#set(CMAKE_CXX_COMPILER "g++")
# 指定生成目标
add_executable(Demo main.c mymath.c)