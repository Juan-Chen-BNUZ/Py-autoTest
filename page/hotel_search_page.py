from poium import Page, PageElement


class HotelSearchPage(Page):
    Hotel_city_input = PageElement(class_name="ant-input ng-pristine ng-valid ant-popover-open ng-touched",
                                   describe="酒店城市框")
    Hotel_city = PageElement(class_name="span-hover", describe="选择城市")
    Begin_date_input = PageElement(class_name="ant-calendar-input-wrap", describe="入住日期框")
    Begin_date = PageElement(
        class_name="ant-calendar-cell ant-calendar-today ant-calendar-selected-day ng-star-inserted",
        describe="选择入住日期")
    End_date_input = PageElement(class_name="ant-calendar-input-wrap",describe="选择离店日期框")
    End_date = PageElement(class_name="ant-calendar-cell ng-star-inserted",describe="选择离店日期")
    Hotel_search = PageElement(class_name="ant-btn ant-btn-primary",describe="搜索按钮")
