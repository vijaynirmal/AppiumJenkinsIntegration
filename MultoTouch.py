import os
import unittest,time
from appium import webdriver
import xmlrunner
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction


class Appium_fb(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'ZX1G3256NJ'
        desired_caps['app'] = 'C:\\Python34\\Appium\\multitouchpro.tests.apk'
        desired_caps['appPackage'] = 'multitouchpro.tests'
        desired_caps['appActivity']= 'Multitouch'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        
    def test_multitouch(self):
        driver = self.driver
        driver.implicitly_wait(90)
        
        action1 = TouchAction(driver)
        action1.long_press(None,1181,665).wait(500).release()
        
        action2 = TouchAction(driver)
        action2.long_press(None,838,1104).wait(500).release()
        
        action3 = TouchAction(driver)
        action3.long_press(None,588,1652).wait(500).release()
        
        multi = MultiAction(driver)
        multi.add(action1,action2,action3)
        multi.perform()
        
        
        
            

        
        
    def tearDown(self):
        self.driver.quit()
        
        
'''if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Appium_fb)
    xmlrunner.XMLTestRunner(output='C:\Python34\Appium\test_reports.xml').run(suite)'''
        
if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='C:\\Python34\\Appium\\test_reports.xml'))
