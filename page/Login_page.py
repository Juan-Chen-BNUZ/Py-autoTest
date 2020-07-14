from poium import Page, PageElement


class LoginPage(Page):
    username = PageElement(xpath='//*[@type="text"]')
    password = PageElement(xpath='//*[@type="password"]')
    button = PageElement(xpath='//*[@nztype="primary"]')
