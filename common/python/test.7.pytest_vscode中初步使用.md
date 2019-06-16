```

```

本文描述在vscode 中使用pytest。

#### 1， pytest 安装

我使用的conda

```
conda install  pytest
```

#### 2，vscode 中配置

vscode 支持单元测试 有unittests，pytest ， nose等，一次只能使用其中一项。

配置开启pytest 单元测试

> 1. 文件-> 首选项->设置
> 2. 搜索 pytest
> 3. 选择  使能pytest

#### 3，编码

##### tt.py

```python
def  add(num):
	return num+1
```

##### test_tt.py

```
import pytest
import tt

def  test_add():
	assert tt.add(2) == 3
	
```

正确配置环境后，在test_add函数上可以看到 “Run Test|Debug Test” 字样。