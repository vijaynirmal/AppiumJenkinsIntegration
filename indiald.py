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
        desired_caps['appPackage'] = 'com.google.android.dialer'
        desired_caps['appActivity']= 'extensions.GoogleDialtactsActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        
    def test_appiumfb(self):
        driver = self.driver
        driver.implicitly_wait(90)
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.dialer:id/contact_tile_name").text("Indiald")').click()
        driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.android.dialer:id/dialpadButton")').click()
        time.sleep(12)
        a1 = TouchAction(driver)
        a1.long_press(None,300,1141,100).release().perform()
        time.sleep(1)
        a1.long_press(None,1130,1703,100).release().perform()
        a1.long_press(None,300,1141,100).release().perform()
        a1.long_press(None,1130,1703,100).release().perform()
        a1.long_press(None,718,1703,100).release().perform()
        a1.long_press(None,718,1703,100).release().perform()
        a1.long_press(None,306,1421,100).release().perform()
        a1.long_press(None,720,1990,100).release().perform()
        a1.long_press(None,300,1141,100).release().perform()
        a1.long_press(None,1136,1415,100).release().perform()
        a1.long_press(None,1136,1415,100).release().perform()
        a1.long_press(None,1138,1136,100).release().perform()
        a1.long_press(None,721,1415,100).release().perform()
        
        
        
        
    def tearDown(self):
        self.driver.quit()
        
        
'''if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Appium_fb)
    xmlrunner.XMLTestRunner(output='C:\Python34\Appium\test_reports.xml').run(suite)'''
        
if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='C:\\Python34\\Appium\\test_reports.xml'))
