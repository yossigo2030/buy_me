from Parser import Parser
from BuyMe import BuyMe
import unittest
import time


class MyTestCase(unittest.TestCase):
    __title = None
    __filePath = "C:\\Users\\YOSSI GOLDBERG\\portland\\pythonProject3\\Untitled.xml"
    __buy_me = None
    __parser = None
    web = "chrome"
    name = "yossi"
    mail = "yossigoldberg6@gmail.com"
    pass1 = "Yg0584176037"
    pass2 = "Yg0584176037"
    title = "BUYME אתר המתנות והחוויות הגדול בישראל | Gift Card"


    @classmethod
    def setUpClass(cls):
        cls.__buy_me = BuyMe(cls.web)
        cls.__title = cls.__buy_me.get_title()
        cls.__buy_me.find_elements()
        cls.__title = cls.__buy_me.getDriver().title

    def test_title(self):
        self.assertEqual(self.title, self.__title, "titles don't match!")

    def test_registration(self):
        self.assertTrue(self.register(), "register_failed!")

    def register(self):
        self.__buy_me.send_keys_name_item(self.name)
        self.__buy_me.send_keys_mail_item(self.mail)
        self.__buy_me.send_keys_password_item(self.pass1)
        self.__buy_me.send_keys_password_confirm_item(self.pass2)
        try:
            self.__buy_me.get_sign_up_item().click()
            self.__buy_me.getDriver().find_element_by_css_selector("img[class = 'arrow']")
            return True
        except:
            return False

    @classmethod
    def tearDownClass(self):
        self.__buy_me.end()


if __name__ == '__main__':
    unittest.main()