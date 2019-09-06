

# CTest



## CTest 是什么？

CTest是CMake的一部分，是一个测试框架，可以将构建，配置，测试，覆盖率等指标更新到[CDash]()或[Dart]()看板工具上。 
 有两种模式：

- 一种是，CMake用来配置和编译一个项目，在CMakeLists.txt中使用特殊的指令来创建和执行测试。CTest用来执行这些测试，并作为可选项更新测试结果到看板服务。
- 一种是，运行脚本(使用跟CMakeLists.txt的语法)来控制测试流程，包括下载 更新代码，配置和构建项目  运行测试。



## Simple Testing

相关命令

```
add_test( testname Exename arg1 arg2 ... )
```



可以使用如下命令查看帮助

```bash
cmake --help-command enable_testing
cmake --help-command add_test
cmake --help-property "<CONFIG>_POSTFIX"
cmake --help-command set_property
```



### 代码示例

```cmake
# 启用测试
enable_testing()
# 测试程序是否成功运行
add_test (test_run Demo 5 2)
# 测试帮助信息是否可以正常提示
add_test (test_usage Demo)
set_tests_properties (test_usage
  PROPERTIES PASS_REGULAR_EXPRESSION "Usage: .* base exponent")
# 测试 5 的平方
add_test (test_5_2 Demo 5 2)
set_tests_properties (test_5_2
 PROPERTIES PASS_REGULAR_EXPRESSION "is 25")
# 测试 10 的 5 次方
add_test (test_10_5 Demo 10 5)
set_tests_properties (test_10_5
 PROPERTIES PASS_REGULAR_EXPRESSION "is 100000")
# 测试 2 的 10 次方
add_test (test_2_10 Demo 2 10)
set_tests_properties (test_2_10
 PROPERTIES PASS_REGULAR_EXPRESSION "is 1024")
```

或者可以使用如下的宏代替



```cmake
# 定义一个宏，用来简化测试工作
macro (do_test arg1 arg2 result)
  add_test (test_${arg1}_${arg2} Demo ${arg1} ${arg2})
  set_tests_properties (test_${arg1}_${arg2}
    PROPERTIES PASS_REGULAR_EXPRESSION ${result})
endmacro (do_test)
 
# 使用该宏进行一系列的数据测试
do_test (5 2 "is 25")
do_test (10 5 "is 100000")
do_test (2 10 "is 1024")
```



执行结果

```ini
Test project F:/Test/Demo/6.2/build
    Start 1: test_run
1/5 Test #1: test_run .........................   Passed    0.43 sec
    Start 2: test_usage
2/5 Test #2: test_usage .......................***Failed  Required regular expression not found.Regex=[Usage: .* base exponent
]  0.42 sec
    Start 3: test_5_2
3/5 Test #3: test_5_2 .........................***Failed  Required regular expression not found.Regex=[is 25
]  0.43 sec
    Start 4: test_10_5
4/5 Test #4: test_10_5 ........................***Failed  Required regular expression not found.Regex=[is 100000
]  0.43 sec
    Start 5: test_2_10
5/5 Test #5: test_2_10 ........................***Failed  Required regular expression not found.Regex=[is 1024
]  0.43 sec

20% tests passed, 4 tests failed out of 5

Total Test time (real) =   2.17 sec

The following tests FAILED:
          2 - test_usage (Failed)
          3 - test_5_2 (Failed)
          4 - test_10_5 (Failed)
          5 - test_2_10 (Failed)
Errors while running CTest
```



```bash
#再build目录下执行
ctest.exe --force-new-ctest-process -C Debug
```

```
ctest -R $regex_matching_test -V -N
```

### 参考链接

1. [ctest官方文档](https://cmake.org/cmake/help/v3.15/manual/ctest.1.html)



CTest



CTest  和其他常用框架 入GTest Catch2等的关系







参考链接

1. [如何在 Visual Studio 2017 及更高版本中使用适用于 C++ 的 CTest](https://docs.microsoft.com/zh-cn/visualstudio/test/how-to-use-ctest-for-cpp?view=vs-2017)
2. [Testing With CTest](https://gitlab.kitware.com/cmake/community/wikis/doc/ctest/Testing-With-CTest)
3. [ctest官方文档](https://cmake.org/cmake/help/v3.15/manual/ctest.1.html)











# CDash

CDash是一个基于Web的开源软件测试服务器。它收集、分析和显示全球各地终端提交的软件测试任务结果。开发人员依赖CDash来传达软件系统的状态，并持续改进软件质量。CDash是一个大型软件任务的一部分，该软件任务集成了Kitware的CMake、CTest和CPack工具，以及用于设计、管理和维护大型软件系统的其他外部包。[CMake](https://open.cdash.org/index.php?project=CMake)质量管理面板和[VTK](https://open.cdash.org/index.php?project=VTK")质量管理面板就是一个好的例子。

[Kitware Inc](https://www.kitware.com/).最近发布了一些[公共管理面板](https://my.cdash.org/)。

[CMake](https://cmake.org/)提供在这些管理面板上发布编译+测试结果、测试集范围和动态分析（内存泄漏）的方法。



参考链接 

1. https://github.com/Kitware/CDash
2. https://open.cdash.org/index.php?project=CDash&date=2019-09-06