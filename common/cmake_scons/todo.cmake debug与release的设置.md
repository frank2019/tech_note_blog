



CMake中有一个变量CMAKE_BUILD_TYPE，可以取值枚举入下：Debug   Release  RelWithDebInfo  和  MinSizeRel



编译定义输出库的前缀



```cmake
if(WIN32 AND NOT MINGW)
  if(NOT DEFINED CMAKE_DEBUG_POSTFIX)
    set(CMAKE_DEBUG_POSTFIX "_debug")
  endif()
  if(NOT DEFINED CMAKE_RELEASE_POSTFIX)
    set(CMAKE_RELEASE_POSTFIX "_release")
  endif()
  if(NOT DEFINED CMAKE_RELWITHDEBINFO_POSTFIX)
    set(CMAKE_RELWITHDEBINFO_POSTFIX "_release")
  endif()
  if(NOT DEFINED CMAKE_MINSIZEREL_POSTFIX)
    set(CMAKE_MINSIZEREL_POSTFIX "_release")
  endif()
endif()

```



可能你的dll没有定义任何输出函数,所以没有生成lib文件.