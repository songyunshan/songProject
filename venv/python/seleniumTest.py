#encoding=utf-8
from selenium import webdriver
import unittest
import time
class TestLogin(unittest.TestCase):
    #每个测试用例执行之前做操作
    def setUp(self):
        # 打开浏览器
        self.driver = webdriver.Chrome("C:\\Users\\sys\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver")
    #登录测测试用例
    def test_Login(self):
        driver = self.driver
        # 打开测试环境url
        driver.get("https://shoptest.boldseas.com/index")
        # 浏览器最大化
        driver.maximize_window()
        #点击登录
        driver.find_element_by_id("loginUrl").click()
        #输入手机号
        driver.find_element_by_id("phone").send_keys(self,"13466628697")
        time.sleep(3)
    def tearDown(self):
        #关闭浏览器
        self.driver.close()



if __name__ == "__main__":
    unittest.main()




