import time
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import unittest

def main():
    #Initialize driver session with the device and get driver handle to use later in the code.
    driver = InitializeSession()

    #Test for selecting a loo, see directions and update rating.
    Test1(driver)

    #Test for adding new loo information.
    Test2(driver)

    #Close test session with the server.
    CloseSession(driver)

def InitializeSession():
    DesiredCaps = {
        'platformName': 'Android',
        'platformVersion': '9',
        'deviceName': 'Android Emulator',
        'automationName': 'UiAutomator2',
        'app': 'E:/Data/cloo/Cloo-master/Cloo-master/Cloo2019/app/build/outputs/apk/debug/app-debug.apk',
        'appWaitDuration': 30000,
        'appPackage': 'com.example.cloo2019',
        'appActivity': '.MainActivity_LocateLoo',
        'deviceReadyTimeout': 5,
        'avd': 'Pixel_API_28'

    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', DesiredCaps)
    return driver

def Test1(driver):
    #Select Allow button to access location services if prompted.
    element = driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button')
    element.click()
    time.sleep(5)

    # Invoke a loo location from the list view to see directions and update rating and/or comments.
    # Invokes second record from the list. In this screen, there are many textviews. Instance 4 corresponds to second item.
    element = driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.TextView").instance(4)')
    element.click()
    time.sleep(5)

    #Select Direction button to see the map
    element = driver.find_element_by_id('com.example.cloo2019:id/button_Navigate')
    element.click()
    time.sleep(5)

    #Select Back button to choose rating, submit and close.
    driver.press_keycode(4)
    time.sleep(5)
    # Update rating and comments
    element = driver.find_element_by_class_name('android.widget.RatingBar')
    actions = ActionChains(driver)
    # Co-ordinates for Ratingbar
    # 5: 580,120
    # 4: 460,120
    # 3: 360,120
    # 2: 240,120
    # 1: 100,120
    actions.move_to_element_with_offset(element, 360, 120)
    actions.perform()
    actions.click()
    actions.perform()
    element = driver.find_element_by_id('com.example.cloo2019:id/button_submit_close')
    element.click()
    time.sleep(5)
    # Select Back button to go back to Loo list view screen.
    driver.press_keycode(4)
    time.sleep(2)

def Test2(driver):
    #Add new loo rating and comments
    element = driver.find_element_by_class_name('android.widget.ImageButton')
    element.click()
    time.sleep(5)
    element = driver.find_element_by_class_name('android.widget.RatingBar')
    actions = ActionChains(driver)
    #Co-ordinates for Ratingbar
    #5: 580,120
    #4: 460,120
    #3: 360,120
    #2: 240,120
    #1: 100,120
    actions.move_to_element_with_offset(element,100,120)
    actions.perform()
    actions.click()
    actions.perform()
    element = driver.find_element_by_class_name('android.widget.EditText')
    element.send_keys('Add comments to this rating.')
    time.sleep(1)
    element = driver.find_element_by_id('com.example.cloo2019:id/button_Submit')
    element.click()


def CloseSession(driver):
    driver.quit


if __name__ == '__main__':
 main()




