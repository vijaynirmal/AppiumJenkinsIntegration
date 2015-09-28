import os
import unittest,time
from appium import webdriver
import xmlrunner
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

class Default_Browser(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'ZX1G3256NJ'
        desired_caps['browserName'] = 'Chrome'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        
    def test_default_browser(self):
        driver = self.driver
        driver.implicitly_wait(90)
        base_url = "https://www.kroger.com"
        driver.get(base_url)
        driver.find_element_by_xpath('.//*[@id="signIn"]').click()
        email_field = driver.find_element_by_xpath('//input [@id="signin-drawer-email-address"]')
        email_field.click()
        email_field.send_keys("mobile.automation7@gmail.com")
        password_field = driver.find_element_by_xpath('.//*[@id="signin-drawer-password"]')
        password_field.click()
        password_field.send_keys("training123")
        driver.find_element_by_xpath('.//*[@id="signin-drawer-submit"]').click()
        time.sleep(5)   

        
    def tearDown(self):
        self.driver.quit()
        
        
'''if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Appium_fb)
    xmlrunner.XMLTestRunner(output='C:\Python34\Appium\test_reports.xml').run(suite)'''
        
if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='C:\\Python34\\Appium\\test_reports1.xml'))
