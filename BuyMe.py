from selenium import webdriver
# from msedge.selenium_tools import EdgeOptions, Edge
from selenium.webdriver.chrome.options import Options

class BuyMe(object):
    __driver = None
    __options = None
    __register_sign_up_item = None
    __register_item = None
    __name_item = None
    __mail_item = None
    __password_item = None
    __confirm_password_item = None
    __sign_up_item = None

    def __init__(self, browser):
        self.web_driver(browser)
        self.__driver.implicitly_wait(1)

    def web_driver(self, browser):
        if browser == "chrome":
            self.chrome_options()
            self.__driver.get("https://buyme.co.il/")
        else:
            self.__driver = webdriver.Edge()
            self.__driver.get("https://buyme.co.il/")

    def chrome_options(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--start-maximized")
        self.__driver = webdriver.Chrome(options=chrome_options)

    def register_sign_up_item(self):
        self.__register_sign_up_item = self.__driver.find_element_by_css_selector("#ember957 > div > ul.nav-bar.buttons > li:nth-child(3) > a > span:nth-child(2)")
        self.__register_sign_up_item.click()

    def register_item(self):
        self.__register_item = self.__driver.find_element_by_class_name("text-link")
        self.__register_item.click()

    def name_item(self):
        self.__name_item = self.__driver.find_element_by_css_selector("input[placeholder = 'שם פרטי']")

    def mail_item(self):
        self.__mail_item = self.__driver.find_element_by_css_selector("input[placeholder = 'מייל']")

    def password_item(self):
        self.__password = self.__driver.find_element_by_css_selector("input[placeholder = 'סיסמה']")

    def confirm_password_item(self):
        self.__confirm_password_item = self.__driver.find_element_by_css_selector("input[placeholder = 'אימות סיסמה']")

    def sign_up_item(self):
        self.__sign_up_item = self.__driver.find_element_by_css_selector("button[gtm = 'הרשמה ל-BUYME']")
        # self.__sign_up_item.click()

    def set_first_name(self, string):
        self.first_name = string

    def set_mail(self, string):
        self.mail = string

    def set_password(self, string):
        self.password = string

    def get_title(self):
        return self.__driver.title

    def send_keys_name_item(self, string):
        self.__name_item.send_keys(string)

    def send_keys_mail_item(self, string):
        self.__mail_item.send_keys(string)

    def send_keys_password_item(self, string):
        self.__password.send_keys(string)

    def send_keys_password_confirm_item(self, string):
        self.__confirm_password_item.send_keys(string)

    def get_sign_up_item(self):
        return self.__sign_up_item

    def getDriver(self):
        return self.__driver

    def end(self):
        self.__driver.close()