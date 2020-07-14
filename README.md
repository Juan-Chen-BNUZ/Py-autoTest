# pyautoTest Web UI 自动化项目

#### 安装：

```shell
$ pip install -r requirements.txt
```
注：安装```requirements.txt```指定依赖库的版本，这是经过测试的，有时候新的版本可会有错。

#### 配置：

在 `config.py` 文件配置

```python
class RunConfig:
    """
    运行测试配置
    """
    # 配置浏览器驱动类型。
    driver_type = "chrome"
    
    # 配置运行的 URL
    url = "https://www.baidu.com"
    
    # 失败重跑次数
    rerun = "3"
    
    # 当达到最大失败数，停止执行
    max_fail = "5"
    
    # 运行测试用例的目录或文件
    cases_path = "./test_dir/"
```
#### 文件注释：
 - 1、page——封装元素定位操作
 - 2、test_dir——存放测试用例
    - 1、data——数据文件，读取数据
 - 3、test_report——测试报告
 
#### 运行：

**支持在pycharm编辑器中运行。如若需要在 cmd（windows）/终端(Linux)下运行，请执行以下指令。**

```shell
$ python run_tests.py  (回归模式，生成HTML报告)
$ python run_tests.py -m debug  (调试模式)
```

#### TODO：

 - 1、登录态存储，试了几个方法，没有什么好效果
 - 2、Log
 - 3、用例完善
 - 4、该框架灵活性比较低，可能需要大改，主要是在conftest.py文件的逻辑(可能是我还没吃透=- =)。就是因为这个问题，登录态才迟迟解决不了


