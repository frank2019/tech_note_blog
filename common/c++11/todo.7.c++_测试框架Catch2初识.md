测试框架Catch2



> 1. Catch2（C++ Automated Test Cases in Headers）
> 2. Catch2是一个header-only测试框架.
> 3. 开源许可证是[Boost license](https://www.boost.org/users/license.html)
> 4. 当前版本是基于C++11开发的，最初版本[Catch1.x](https://github.com/catchorg/Catch2/tree/Catch1.x)是基于C++03/98的。



# Catch2优势和特点

- 简单易用：只需要catch.hpp。
- 不依赖外部库：只要你可以编译C++11，有C++的标准库就可以了
- 测试case可以分割为sections: 每个setcion都是独立的运行单元
- 提供了BDD式的测试模式：可以使用Given-When-Then section来做BDD测试
- 只用一个核心的assertion宏来做比较。用标准的C++运算符来做比较，但是可以分解表达式，记录表达式等号左侧和右侧的值
- 可以用任何形式的字符串给测试命名，不用担名字是否合法。

其它一些关键特性有：

- 可以给test case打tag, 因而可以很容易的只跑某个tag组的test cases
- 输出通过reporter对象完成，支持基本的文本和XML格式输出测试结果，也支持自定义reporter
- 支持JUnit xml输出，这样可以和第三方工具整合，如CI服务器等
- 提供默认的main()函数，用户也可以使用自己的main()函数
- 提供一个命令行解析工具，用户在使用自己的main()函数的时候可以添加命令行参数
- catch软件可以做自测试
- 提供可选的assertion宏，可以报告错误但不终止test case
- 通过内置的Approx()语法支持可控制精度的浮点数比较
- 通过Matchers支持各种形式的比较，也支持自定义的比较方法



编译

```c++
g++ -std=c++11 -o catchTest catchTest.cpp -I/usr/local/include/
```



# TEST_CASE

> 1. **TEST_CASE(** *test name* [, *tags* ] **)**
> 2. *SECTION(** *section name* **)**



- 一般的测试框架都采用基于类的test fixture, 通常需要定义setup()和teardown()函数（或者在构造/析构函数中做类似的事情）。catch不仅全面支持[test fixture](https://github.com/catchorg/Catch2/blob/master/docs/test-fixtures.md#top)模式，还提供了一种section机制：每个section都是独立运行单元。

- 对于每个section来说，它都从test case的最开始运行，也就是说它们共享前半部分的代码，这些section不是并发执行的，而是每次执行一个section。

- 每个TEST_CASE的执行是  

  ```
  init --> section1  --->release
  init --> section2  --->release
  ```

  其中

  1. init 部分test_case 开始到 第一个section
  2. release 部分代表 最后一个section 到test_case结束



# Assertion基本断言



    REQUIRE(expression)
    CHECK(expression)
    REQUIRE_FALSE(expression)
    CHECK_FALSE(expression)


注意：REQUIRE和CHECK最主要的区别在于

- REQUIRE表达式为false时中断执行，而CHECK继续执行。



# Matcher比较器

    REQUIRE_THAT(lhs, matcher expression)
    CHECK_THAT(lhs, matcher expression)
    主要内置Matchers
    – string matchers:StartsWith, EndsWith, Contains, Equals and Matches
    – vector matchers:Contains, VectorContains and Equals
    – floating point matchers:WithinULP and WithinAbs
    
    REQUIRE_THAT( str, EndsWith( "as a service", Catch::CaseSensitive::No ) ); 
        1

# 浮点数比较

    epsilon:default std::numeric_limits::epsilon()*100.
    margin:default 0.0.
    scale:default 0.0.
```c++
TEST_CASE("approx epsilon", "[single-file]") 
{ 
	// 闭区间 
	// [100-100*epsilon,100+100*epsilon] 
	Approx target = Approx(100).epsilon(0.01); 
	CHECK(100.0 == target); // Obviously true 
	CHECK(99.0 == target); // Obviously true 
	CHECK(98.1 == target); // Obviously true 
	CHECK(101.0 == target); // Obviously true 
	CHECK(101.1 == target); // Obviously true 
	
} 
TEST_CASE("approx margin", "[single-file]") { 
	// 闭区间 
	// [100-margin,100+margin] 
	Approx target = Approx(100).margin(1); 
	CHECK(100.0 == target); // Obviously true 
	CHECK(99.0 == target); // Obviously true 
	CHECK(98.1 == target); // Obviously true 
	CHECK(101.0 == target); // Obviously true 
	CHECK(101.1 == target); // Obviously true	
}

```

# Logging

    INFO( message expression )
    WARN( message expression )
    FAIL( message expression )
    FAIL_CHECK( message expression )
    CAPTURE( expression1, expression2, … )
使用说明

> 1. INFO ,CAPTURE 会在所在case 报错的时候打印出来
> 2. WARN  运行的时候会直接打印
> 3. FAIL，FAIL_CHECK  会直接打印出来，并终止测试

# 命令行使用

## Uasge

```bash

Catch v2.5.0
usage:
  depth-apis-unit-test.exe [<test name|pattern|tags> ... ] options

where options are:
  -?, -h, --help                            display usage information
  -l, --list-tests                          list all/matching test cases
  -t, --list-tags                           list all/matching tags
  -s, --success                             include successful tests in
                                            output
  -b, --break                               break into debugger on failure
  -e, --nothrow                             skip exception tests
  -i, --invisibles                          show invisibles (tabs, newlines)
  -o, --out <filename>                      output filename
  -r, --reporter <name>                     reporter to use (defaults to
                                            console)
  -n, --name <name>                         suite name
  -a, --abort                               abort at first failure
  -x, --abortx <no. failures>               abort after x failures
  -w, --warn <warning name>                 enable warnings
  -d, --durations <yes|no>                  show test durations
  -f, --input-file <filename>               load test names to run from a
                                            file
  -#, --filenames-as-tags                   adds a tag for the filename
  -c, --section <section name>              specify section to run
  -v, --verbosity <quiet|normal|high>       set output verbosity
  --list-test-names-only                    list all/matching test cases
                                            names only
  --list-reporters                          list all reporters
  --order <decl|lex|rand>                   test case order (defaults to
                                            decl)
  --rng-seed <'time'|number>                set a specific seed for random
                                            numbers
  --use-colour <yes|no>                     should output be colourised
  --libidentify                             report name and version according
                                            to libidentify standard
  --wait-for-keypress <start|exit|both>     waits for a keypress before
                                            exiting
  --benchmark-resolution-multiple           multiple of clock resolution to
  <multiplier>                              run benchmarks

For more detailed usage please see the project docs
```

## 常用命令

- 显示test case总体情况：  test -l
- 显示所有的标签（tags）:  test -t
- 运行某个tag下的所有test cases:   test [tag]
- 运行某个名字的test case:  test   "name"
- 运行指定的section   ：   test -c  section_name



# 参考链接

1. [Catch2 github项目主页](https://github.com/catchorg/Catch2)
2. [Writing C++ unit tests with Catch2](https://mariusbancila.ro/blog/2018/03/29/writing-cpp-unit-tests-with-catch2/)
3. [测试C++程序：使用Catch和Valgrind](https://www.jianshu.com/p/6f03a0cfe60c)
4. [**catch2:一个好用的C++单元测试框架**](https://blog.csdn.net/ithiker/article/details/87909651)

