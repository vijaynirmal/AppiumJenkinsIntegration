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
        desired_caps['app'] = 'C:\\Python34\\Appium\\com.mobeta.android.demodslv-0.5.0-3_APKdot.com.apk'
        desired_caps['appPackage'] = 'com.mobeta.android.demodslv'
        desired_caps['appActivity']= 'Launcher'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        
    def test_appiumfb(self):
        driver = self.driver
        driver.implicitly_wait(90)
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.mobeta.android.demodslv:id/activity_title").text("Warp")').click()
        
        driver.swipe(1258,433,172,412,800)
        
        x = driver.find_elements_by_id("com.mobeta.android.demodslv:id/text")[0]
        
        if x.text == "Albania" :
            pass
        else :
            print ("oops swipe didnt work properly")
            

        
        
    def tearDown(self):
        self.driver.quit()
        
        
'''if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Appium_fb)
    xmlrunner.XMLTestRunner(output='C:\Python34\Appium\test_reports.xml').run(suite)'''
        
if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='C:\\Python34\\Appium\\test_reports.xml'))
