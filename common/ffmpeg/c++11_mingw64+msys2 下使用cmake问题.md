



# mingw64+msys2 下使用cmake问题





直接pacman -S cmake 安装的并不好用，直接下载windows版本的cmake. 比如安装在D:\\cmake下. 然后设置环境变量

export PATH=C:/cmake/bin:$PATH 

然后编辑一个 toolchain-mingw64.cmake文件:



```
SET(CMAKE_SYSTEM_NAME Windows)
SET(CMAKE_C_COMPILER x86_64-w64-mingw32-gcc)
SET(CMAKE_CXX_COMPILER x86_64-w64-mingw32-g++)
SET(CMAKE_RC_COMPILER x86_64-w64-mingw32-windres)
SET(CMAKE_RANLIB x86_64-w64-mingw32-ranlib)

SET(CMAKE_ASM_YASM_COMPILER yasm)

```

保存后。

接下来: cmake -G"Unix Makefiles" . -DCMAKE_TOOLCHAIN_FILE=toolchain-mingw64.cmake 就可以生成makefile文件.

注意上面的 toolchain-mingw64.cmake内容 这些变量可能要根据实际情况设置。

还有个问题，mingw64生成的dll往往依赖libgccxxx.dll 和 libstdc++.dll, 如何不依赖，给 toolchain-mingw64.cmake加入下面的代码即可

SET(CMAKE_CXX_FLAGS "-static-libgcc -static-libstdc++ -static")
SET(CMAKE_C_FLAGS "-static-libgcc -static-libstdc++ -static")
SET(CMAKE_SHARED_LIBRARY_LINK_C_FLAGS "-static-libgcc -static-libstdc++ -static")

SET(CMAKE_SHARED_LIBRARY_LINK_CXX_FLAGS "-static-libgcc -static-libstdc++ -static")

到此为止应该能帮你解决掉部分问题。
