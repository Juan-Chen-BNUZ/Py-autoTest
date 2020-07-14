"""
@author:  虫师
@data: 2019-10-17
@function pytest 参数使用
"""
import sys
import json
from time import sleep
import pytest
from os.path import dirname, abspath

from test_dir.data.get_data import GetData

base_path = dirname(dirname(abspath(__file__)))
sys.path.insert(0, base_path)
from page.Login_page import LoginPage


@pytest.mark.parametrize(
    "name,word", [(GetData("Login").get_value("username"), GetData("Login").get_value("password"))])
def test_login_search(name, word, browser, base_url):
    page = LoginPage(browser)
    page.get(base_url + "/passport/login")
    page.username = name
    page.password = word
    page.button.click()
    browser.implicitly_wait(60)
    assert "让差旅更便捷" in browser.title


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_login.py"])
