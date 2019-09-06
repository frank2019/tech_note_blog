# 查找当前目录下的所有源文件
# 并将名称保存到 DIR_LIB_SRCS 变量
aux_source_directory(. DIR_LIB_SRCS)
# 生成链接库
add_library (MathFunctions ${DIR_LIB_SRCS})

include(${CMAKE_ROOT}/Modules/CheckSymbolExists.cmake)
CHECK_SYMBOL_EXISTS(FibonacciSequence ${PROJECT_SOURCE_DIR}/math/mymath.h  HAVE_POW1)
message("FibonacciSequence is  ${HAVE_POW1}")
