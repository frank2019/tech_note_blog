# cppcheck 

## 1，简介

cppcheck 是一个静态代码检查工具，支持c, c++ 代码；作为编译器的一种补充检查，cppcheck对产品的源代码执行严格的逻辑检查。 



## 2，检查内容

Cppcheck是c/c++代码的静态分析工具。Cppcheck 不是一个风格检查工具也不是语法错误检查。它提供了独特的代码分析来检测bug，并着重于检测未定义的行为和危险的编码结构。

1. 自动变量检查
2. 数组的边界检查
3. class类检查
4. 过期的函数，废弃函数调用检查
5. 异常内存使用，释放检查
6. 内存泄漏检查，主要是通过内存引用指针
7. 操作系统资源释放检查，中断，文件描述符等
8. 异常STL 函数使用检查
9. 代码格式错误，以及性能因素检查



## 3，安装

### windows下的安装

在linux中类似。

1. 从http://cppcheck.net/下载并安装msi文件，

2. 默认安装到C:\Program Files\Cppcheck，

3. 将C:\Program Files\Cppcheck添加path环境变量，便于以后的使用。  


### vs中配置

在vs1020中做如下设置，即可在vs的输出窗口中看到cppcheck的检查结果，当然可以随时修改cppcheck的级别

属性-> 生成事件->预先生成事件->命令行

```bash
cppcheck --enable=all --project=$(ProjectFileName)
```

在生成中使用  选择 是。

### Debian:

```bash
sudo apt-get install cppcheck
```

### Fedora:

```bash
sudo yum install cppcheck
```

### Mac:

```bash
brew install cppcheck
```



### Clients and plugins

Cppcheck is integrated with many popular development tools. For instance:

- **CLion** - [Cppcheck plugin](https://plugins.jetbrains.com/plugin/8143)
- **Codacy** - [integrated](https://www.codacy.com/) - Check for code style and security issues on every commit and pull request
- **Code::Blocks** - *integrated*
- **CodeDX** (software assurance tool) - [integrated](http://codedx.com/code-dx-standard/)
- **CodeLite** - *integrated*
- **CppDepend 5** - [integrated](http://www.cppdepend.com/CppDependV5.aspx)
- **Eclipse** - [Cppcheclipse](https://github.com/kwin/cppcheclipse/wiki/Installation)
- **KDevelop** - [integrated since v5.1](https://kdevelop.org/)
- **gedit** - [gedit plugin](http://github.com/odamite/gedit-cppcheck)
- **Hudson** - [Cppcheck Plugin](http://wiki.hudson-ci.org/display/HUDSON/Cppcheck+Plugin)
- **Jenkins** - [Cppcheck Plugin](http://wiki.jenkins-ci.org/display/JENKINS/Cppcheck+Plugin)
- **Mercurial (Linux)** - [pre-commit hook](http://sourceforge.net/p/cppcheck/wiki/mercurialhook/) - Check for new errors on commit (requires interactive terminal)
- **Tortoise SVN** - [Adding a pre-commit hook script](http://omerez.com/automatic-static-code-analysis/)
- **Git (Linux)** - [pre-commit hook](https://github.com/danmar/cppcheck/blob/master/tools/git-pre-commit-cppcheck) - Check for errors in files going into commit (requires interactive terminal)
- **Visual Studio** - [Visual Studio plugin](https://github.com/VioletGiraffe/cppcheck-vs-addin/releases/latest)
- **QtCreator** - [Qt Project Tool (qpt)](https://sourceforge.net/projects/qtprojecttool/files)

## 4，命令行的使用

```ini
Cppcheck - A tool for static C/C++ code analysis

Syntax:
    cppcheck [OPTIONS] [files or paths]

If a directory is given instead of a filename, *.cpp, *.cxx, *.cc, *.c++, *.c,
*.tpp, and *.txx files are checked recursively from the given directory.

Options:
    --addon=<addon>
                         Execute addon. i.e. cert.
    --cppcheck-build-dir=<dir>
                         Analysis output directory. Useful for various data.
                         Some possible usages are; whole program analysis,
                         incremental analysis, distributed analysis.
    --check-config       Check cppcheck configuration. The normal code
                         analysis is disabled by this flag.
    --check-library      Show information messages when library files have
                         incomplete info.
    --config-exclude=<dir>
                         Path (prefix) to be excluded from configuration
                         checking. Preprocessor configurations defined in
                         headers (but not sources) matching the prefix will not
                         be considered for evaluation.
    --config-excludes-file=<file>
                         A file that contains a list of config-excludes
    --doc                Print a list of all available checks.
    --dump               Dump xml data for each translation unit. The dump
                         files have the extension .dump and contain ast,
                         tokenlist, symboldatabase, valueflow.
    -D<ID>               Define preprocessor symbol. Unless --max-configs or
                         --force is used, Cppcheck will only check the given
                         configuration when -D is used.
                         Example: '-DDEBUG=1 -D__cplusplus'.
    -U<ID>               Undefine preprocessor symbol. Use -U to explicitly
                         hide certain #ifdef <ID> code paths from checking.
                         Example: '-UDEBUG'
    -E                   Print preprocessor output on stdout and don't do any
                         further processing.
    --enable=<id>        Enable additional checks. The available ids are:
                          * all
                                  Enable all checks. It is recommended to only
                                  use --enable=all when the whole program is
                                  scanned, because this enables unusedFunction.
                          * warning
                                  Enable warning messages
                          * style
                                  Enable all coding style checks. All messages
                                  with the severities 'style', 'performance' and
                                  'portability' are enabled.
                          * performance
                                  Enable performance messages
                          * portability
                                  Enable portability messages
                          * information
                                  Enable information messages
                          * unusedFunction
                                  Check for unused functions. It is recommend
                                  to only enable this when the whole program is
                                  scanned.
                          * missingInclude
                                  Warn if there are missing includes. For
                                  detailed information, use '--check-config'.
                         Several ids can be given if you separate them with
                         commas. See also --std
    --error-exitcode=<n> If errors are found, integer [n] is returned instead of
                         the default '0'. '1' is returned
                         if arguments are not valid or if no input files are
                         provided. Note that your operating system can modify
                         this value, e.g. '256' can become '0'.
    --errorlist          Print a list of all the error messages in XML format.
    --exitcode-suppressions=<file>
                         Used when certain messages should be displayed but
                         should not cause a non-zero exitcode.
    --file-list=<file>   Specify the files to check in a text file. Add one
                         filename per line. When file is '-,' the file list will
                         be read from standard input.
    -f, --force          Force checking of all configurations in files. If used
                         together with '--max-configs=', the last option is the
                         one that is effective.
    -h, --help           Print this help.
    -I <dir>             Give path to search for include files. Give several -I
                         parameters to give several paths. First given path is
                         searched for contained header files first. If paths are
                         relative to source files, this is not needed.
    --includes-file=<file>
                         Specify directory paths to search for included header
                         files in a text file. Add one include path per line.
                         First given path is searched for contained header
                         files first. If paths are relative to source files,
                         this is not needed.
    --include=<file>
                         Force inclusion of a file before the checked file. Can
                         be used for example when checking the Linux kernel,
                         where autoconf.h needs to be included for every file
                         compiled. Works the same way as the GCC -include
                         option.
    -i <dir or file>     Give a source file or source file directory to exclude
                         from the check. This applies only to source files so
                         header files included by source files are not matched.
                         Directory name is matched to all parts of the path.
    --inconclusive       Allow that Cppcheck reports even though the analysis is
                         inconclusive.
                         There are false positives with this option. Each result
                         must be carefully investigated before you know if it is
                         good or bad.
    --inline-suppr       Enable inline suppressions. Use them by placing one or
                         more comments, like: '// cppcheck-suppress warningId'
                         on the lines before the warning to suppress.
    -j <jobs>            Start <jobs> threads to do the checking simultaneously.
    --language=<language>, -x <language>
                         Forces cppcheck to check all files as the given
                         language. Valid values are: c, c++
    --library=<cfg>      Load file <cfg> that contains information about types
                         and functions. With such information Cppcheck
                         understands your code better and therefore you
                         get better results. The std.cfg file that is
                         distributed with Cppcheck is loaded automatically.
                         For more information about library files, read the
                         manual.
    --max-ctu-depth=N    Max depth in whole program analysis. The default value
                         is 2. A larger value will mean more errors can be found
                         but also means the analysis will be slower.
    --output-file=<file> Write results to file, rather than standard error.
    --project=<file>     Run Cppcheck on project. The <file> can be a Visual
                         Studio Solution (*.sln), Visual Studio Project
                         (*.vcxproj), compile database (compile_commands.json),
                         or Borland C++ Builder 6 (*.bpr). The files to analyse,
                         include paths, defines, platform and undefines in
                         the specified file will be used.
    --max-configs=<limit>
                         Maximum number of configurations to check in a file
                         before skipping it. Default is '12'. If used together
                         with '--force', the last option is the one that is
                         effective.
    --platform=<type>, --platform=<file>
                         Specifies platform specific types and sizes. The
                         available builtin platforms are:
                          * unix32
                                 32 bit unix variant
                          * unix64
                                 64 bit unix variant
                          * win32A
                                 32 bit Windows ASCII character encoding
                          * win32W
                                 32 bit Windows UNICODE character encoding
                          * win64
                                 64 bit Windows
                          * avr8
                                 8 bit AVR microcontrollers
                          * native
                                 Type sizes of host system are assumed, but no
                                 further assumptions.
                          * unspecified
                                 Unknown type sizes
    --plist-output=<path>
                         Generate Clang-plist output files in folder.
    -q, --quiet          Do not show progress reports.
    -rp, --relative-paths
    -rp=<paths>, --relative-paths=<paths>
                         Use relative paths in output. When given, <paths> are
                         used as base. You can separate multiple paths by ';'.
                         Otherwise path where source files are searched is used.
                         We use string comparison to create relative paths, so
                         using e.g. ~ for home folder does not work. It is
                         currently only possible to apply the base paths to
                         files that are on a lower level in the directory tree.
    --report-progress    Report progress messages while checking a file.
    --rule=<rule>        Match regular expression.
    --rule-file=<file>   Use given rule file. For more information, see:
                         http://sourceforge.net/projects/cppcheck/files/Articles/
    --std=<id>           Set standard.
                         The available options are:
                          * c89
                                 C code is C89 compatible
                          * c99
                                 C code is C99 compatible
                          * c11
                                 C code is C11 compatible (default)
                          * c++03
                                 C++ code is C++03 compatible
                          * c++11
                                 C++ code is C++11 compatible
                          * c++14
                                 C++ code is C++14 compatible
                          * c++17
                                 C++ code is C++17 compatible
                          * c++20
                                 C++ code is C++20 compatible (default)
    --suppress=<spec>    Suppress warnings that match <spec>. The format of
                         <spec> is:
                         [error id]:[filename]:[line]
                         The [filename] and [line] are optional. If [error id]
                         is a wildcard '*', all error ids match.
    --suppressions-list=<file>
                         Suppress warnings listed in the file. Each suppression
                         is in the same format as <spec> above.
    --template='<text>'  Format the error messages. Available fields:
                           {file}              file name
                           {line}              line number
                           {column}            column number
                           {callstack}         show a callstack. Example:
                                                 [file.c:1] -> [file.c:100]
                           {inconlusive:text}  if warning is inconclusive, text
                                               is written
                           {severity}          severity
                           {message}           warning message
                           {id}                warning id
                           {cwe}               CWE id (Common Weakness Enumeration)
                           {code}              show the real code
                           \t                 insert tab
                           \n                 insert newline
                           \r                 insert carriage return
                         Example formats:
                         '{file}:{line},{severity},{id},{message}' or
                         '{file}({line}):({severity}) {message}' or
                         '{callstack} {message}'
                         Pre-defined templates: gcc, vs, edit.
    --template-location='<text>'
                         Format error message location. If this is not provided
                         then no extra location info is shown.
                         Available fields:
                           {file}      file name
                           {line}      line number
                           {column}    column number
                           {info}      location info
                           {code}      show the real code
                           \t         insert tab
                           \n         insert newline
                           \r         insert carriage return
                         Example format (gcc-like):
                         '{file}:{line}:{column}: note: {info}\n{code}'
    -v, --verbose        Output more detailed error information.
    --version            Print out version number.
    --xml                Write results in xml format to error stream (stderr).
    --xml-version=<version>
                         Select the XML file version. Currently only versions 2 is available.
Example usage:
  # Recursively check the current folder. Print the progress on the screen and
  # write errors to a file:
  cppcheck . 2> err.txt

  # Recursively check ../myproject/ and don't print progress:
  cppcheck --quiet ../myproject/

  # Check test.cpp, enable all checks:
  cppcheck --enable=all --inconclusive --std=posix test.cpp

  # Check f.cpp and search include files from inc1/ and inc2/:
  cppcheck -I inc1/ -I inc2/ f.cpp

For more information:
    http://cppcheck.net/manual.pdf

Many thanks to the 3rd party libraries we use:
 * tinyxml2 -- loading project/library/ctu files.
 * picojson -- loading compile database.
 * pcre -- rules.
 * qt -- used in GUI
```



可参考手册[Cppcheck-manual](c++11_Cppcheck-manual.md)



## 5，参考链接

1. [Cppcheck -A tool for static C/C++ code analysis](http://cppcheck.net/)
2. https://www.cnblogs.com/lidabo/p/3489645.html
3. [cppcheck手册](http://cppcheck.net/manual.html)
4. https://github.com/danmar/cppcheck/