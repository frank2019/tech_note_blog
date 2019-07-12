

# 概述

动态库文件 可执行文件`(.dll，.lib ,.exe, elf)`等格式文件。

在编程开发或者调试部署中，经常需要查看这些文件的信息，无论在windows，还是在Linux平台，常用的编译器都给我们提供一些工具。

# 常用命令



## dumpbin

来源：  Visual Studio附带工具dumpbin.exe

```bash
dumpbin
Microsoft (R) COFF/PE Dumper Version 14.00.24215.1
Copyright (C) Microsoft Corporation.  All rights reserved.

用法: DUMPBIN [选项] [文件]

  选项:

   /ALL
   /ARCHIVEMEMBERS
   /CLRHEADER
   /DEPENDENTS
   /DIRECTIVES
   /DISASM[:{BYTES|NOBYTES}]
   /ERRORREPORT:{NONE|PROMPT|QUEUE|SEND}
   /EXPORTS
   /FPO
   /HEADERS
   /IMPORTS[:文件名]
      /LINENUMBERS
   /LINKERMEMBER[:{1|2}]
   /LOADCONFIG
   /NOLOGO
      /OUT:filename
   /PDATA
   /PDBPATH[:VERBOSE]
   /RANGE:vaMin[,vaMax]
   /RAWDATA[:{NONE|1|2|4|8}[,#]]
   /RELOCATIONS
   /SECTION:名称
   /SUMMARY
   /SYMBOLS
   /TLS
   /UNWINDINFO
```

