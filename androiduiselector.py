import os
import unittest,time
from appium import webdriver
import xmlrunner

class Appium_fb(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'ZX1G3256NJ'
        desired_caps['app'] = 'C:\\Python34\\Appium\\com.facebook.katana-26.0.0.0.1-6036640-minAPI14.apk'
        desired_caps['appPackage'] = 'com.facebook.katana'
        desired_caps['appActivity']= 'com.facebook.katana.LoginActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        
    def test_appiumfb(self):
        driver = self.driver
        driver.implicitly_wait(90)
        user_name_field = driver.find_element_by_id("com.facebook.katana:id/login_username")
        user_name_field.click()
        user_name_field.send_keys("sjvijay86@gmail.com")
        password = driver.find_element_by_id("com.facebook.katana:id/login_password")
        password.click()
        password.send_keys("oldalfer86")
        login_button = driver.find_element_by_id("com.facebook.katana:id/login_login")
        login_button.click()
        not_now = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/dbl_off")')
        not_now.click()
        '''try :
            driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/fbui_megaphone_secondary_button")').click()
        except :
            pass'''
        status_button = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/publisher_button0")')
        status_button.click()
        '''try:
            skip_button = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/skip_link")')
            skip_button.click()
            tool_desc = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/fbui_tooltip_description")')
            tool_desc.click()
        except :
            pass'''
        text_box = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/status_content_wrapper")')
        text_box.click()
        text_box.send_keys("test")
        post_button = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/composer_primary_named_button")')
        post_button.click()
        
        drop_down = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/header_view_menu_button")')
        drop_down.click()
        
        #driver.switch_to_frame(driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/fbui_popover_view_flipper")'))
        
        delete_post_button = driver.find_element_by_android_uiautomator('new UiSelector().text("Delete")')
        delete_post_button.click()
        
        #driver.switch_to_frame(driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/parentPanel")'))
        delete_button_final = driver.find_element_by_android_uiautomator('new UiSelector().text("Delete")')

        delete_button_final.click()
        time.sleep(3)
       
        book_mark = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/bookmarks_tab")')
        book_mark.click()
        
        '''element1 = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/news_feed_tab")')
        element2 = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.facebook.katana:id/fbui_content_view_title").text("Log Out"))')
        driver.scroll(element1,element2)
        element2.click()'''
        
        
    def tearDown(self):
        self.driver.quit()
        
        
'''if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Appium_fb)
    xmlrunner.XMLTestRunner(output='C:\Python34\Appium\test_reports.xml').run(suite)'''
        
if __name__ == "__main__":
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='C:\\Python34\\Appium\\test_reports.xml'))
