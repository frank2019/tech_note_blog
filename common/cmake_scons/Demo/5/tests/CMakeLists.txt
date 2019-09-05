# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量

#TEST 模块版本定义
set (TEST_VERSION_MAJOR 1)
set (TEST_VERSION_MINOR 0)
set (TEST_VERSION_PATCHLEVEL 1)
set (TEST_VERSION_RELEASER 1)


configure_file (
  "test_version.h.ini"
  "${PROJECT_BINARY_DIR}/test_version.h"
  )
include_directories(${PROJECT_BINARY_DIR})

aux_source_directory(. DIR_LIB_SRCS)
# 生成链接库
add_library (Tests ${DIR_LIB_SRCS})