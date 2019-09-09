

透过git submodule 和 CMake 使用 GoogleTest



```
$ cd /path/project
$ git submodule add https://github.com/google/googletest/tree/master/googletest 3rdParty/googletest 
```

 

```cmake
add_subdirectory(3rdParty/googletest) 
add_executable(your_unit_test  your_unit_test.cpp ) 

add_dependencies(your_unit_test gtest)

include_directories(${gtest_SOURCE_DIR}/include) 
target_link_libraries(your_unit_test  gtest ) 
```

