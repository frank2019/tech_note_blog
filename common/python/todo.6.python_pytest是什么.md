

#### `pytest` 特点

pytest是一个非常成熟的全功能的Python测试框架，主要有以下几个特点：

- 简单灵活，容易上手
- 支持参数化
- 能够支持简单的单元测试和复杂的功能测试，还可以用来做selenium/appnium等自动化测试、接口自动化测试（pytest+requests）
- `pytest`具有丰富第三方插件，良好的自定义扩展
- 测试用例的skip和xfail处理
- 可以很好的和jenkins集成
- report框架----allure 也支持了pytest

#### pytest支持那的插件


完整的插件list，可以到下面这三个站点看看：

1. https://docs.pytest.org/en/latest/plugins.html

2. https://pypi.python.org

3. https://github.com/pytest-dev

下面是一些出名的插件list:

- pytest-repeat: 可以多次运行测试用例，用来提高发现那些偶然错误的几率
- pytest-xdist: 可以利用机器的多核，提升测试的速度
- pytest-timeout: 可以为测试加入超时
- pytest-instatfail: 在错误发生的时候，立即报告它
- pytest-sugar: 整合了pytest-instatfail以及代码高亮，颜色字体...
- pytest-emoji: 为测试报告加入了一些有趣的东西
- pytest-html: 在测试完成后，会生成一份html报告文件
- pytest-pycodestyle, pytest-pep8, pytest-flake8: 进行代码规范检查
- pytest-rerunfailures（失败case重复执行）
- pytest-selenium
- pytest-django
- pytest-flask    



pytest

#### 参考链接

1. [unittest和pytest对比](https://www.cnblogs.com/xiaohuhu/p/9804527.html)