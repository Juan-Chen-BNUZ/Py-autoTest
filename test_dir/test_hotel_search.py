import sys
from time import sleep
import pytest
from os.path import dirname, abspath
import conftest
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.hotel_search_page import HotelSearchPage


class TestHotelSearch:
    """酒店搜索"""

    # def setup_module(self):
    #     print("123")
    #     self.browser = conftest.browser
    #     self.url = conftest.base_url + "/hotel/search"
    #
    # def setup(self):
    #     self.page = HotelSearchPage(self.browser)

    def test_hotel_search_case(self,browser, base_url):
        page = HotelSearchPage(browser)
        page.get(base_url+"/hotel/search")
        page.Hotel_city_input.click()
        page.Hotel_city.click()
        page.Begin_date_input.click()
        page.Begin_date.click()
        page.End_date_input.click()
        page.End_date.click()
        page.Hotel_search().click()
        # 等待页面跳转
        browser.implicitly_wait(60)
        assert browser.find_element_by_id("display_info_map")

    # def teardown(self):
    #     conftest.browser_close()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_hotel_search.py"])
