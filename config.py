

class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = "./test_dir/"

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 配置运行的 URL
    url = "https://test-web-te-yi-xing-env-3.teyixing.com"

    # 登录态存储
    option_address = "C:/Users/test/AppData/Local/Google/Chrome/User Data/Default"

    # # 失败重跑次数
    # rerun = "1"
    #
    # # 当达到最大失败数，停止执行
    # max_fail = "5"


