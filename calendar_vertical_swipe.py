import os
import unittest,time
from appium import webdriver
import xmlrunner
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.wait import WebDriverWait


class Calendar_Vertical_Swipe(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'ZX1G3256NJ'
        desired_caps['appPackage'] = 'com.google.android.calendar'
        desired_caps['appActivity']= 'com.android.calendar.AllInOneActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        
    def test_calendar_vertical_swipe(self):
        driver = self.driver
        driver.implicitly_wait(90)
        
        '''if WebDriverWait(driver,10).until(driver.find_element_by_id("com.android.calendar:id/right_arrow")):
            driver.find_element_by_id("com.android.calendar:id/right_arrow").click()
        else :
            pass
        
        if  driver.find_element_by_id("com.android.calendar:id/right_arrow").exists():
            driver.find_element_by_id("com.android.calendar:id/right_arrow").click()
        else :
            pass
        
        if  driver.find_element_by_id("com.android.calendar:id/right_arrow").exists():
            driver.find_element_by_id("com.android.calendar:id/right_arrow").click()
        else :
            pass
        
        if  driver.find_element_by_id("com.android.calendar:id/done_button").exists():
            driver.find_element_by_id("com.android.calendar:id/done_button").click()
        else :
            pass'''
        
        '''driver.find_element_by_id("com.android.calendar:id/right_arrow")click()
        driver.find_element_by_id("com.android.calendar:id/right_arrow").click()
        driver.find_element_by_id("com.android.calendar:id/done_button").click()'''
        
        driver.swipe(872,737,726,2291,800)
        time.sleep(3)
        driver.swipe(636,2211,803,518,800)
        time.sleep(3)

        
        
    def tearDown(self):
        self.driver.quit()
        
        
'''if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Appium_fb)
    xmlrunner.XMLTestRunner(output='C:\Python34\Appium\test_reports.xml').run(suite)'''
        
if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='C:\\Python34\\Appium\\test_reports.xml'))
