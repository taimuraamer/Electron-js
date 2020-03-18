import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from keyboard import press


class unitTest(unittest.TestCase):
    def setUp(self):
        chromedriver_path = r'C:\\Users\\AAI\\Desktop\\chromedriver_win32\\chromedriver.exe'
        electron_path = r"C:\\Users\\AAI\\AppData\\Local\\Programs\\ui.ep.launcher\\AAI-EP.exe"
        opts = Options()
        # opts.add_argument("--remote-debugging-port=8001")
        # opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--start-maximized")
        opts.binary_location = electron_path
        self.driver = webdriver.Chrome(executable_path=chromedriver_path, options=opts)
        self.driver.implicitly_wait(10)  # seconds

    # wait for application to start
    def test_create_testcase(self):
        self.driver.find_element_by_css_selector("#TD-btn_createtest > div").click()  # Create test

        # setting focus to element
        element = self.driver.find_element_by_xpath('//*[@id="TC-GF-radios_testtype"]/div/div/div/div[2]/label')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        # End of Focus

        self.driver.find_element_by_xpath('//*[@id="TC-GF-radios_testtype"]/div/div/div/div[2]/label').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector("#TCF-btn_next > div").click()
        self.driver.find_element_by_css_selector("#TCF-btn_next > div").click()
        self.driver.find_element_by_css_selector("#TCF-btn_next > div").click()
        self.driver.find_element_by_css_selector("#TCF-btn_createtest > div").click()
        # asserting creation of test
        start_btn = self.driver.find_element_by_id("TCC-btn_start_TD-creating0").text
        self.assertEqual("START", start_btn)
        self.driver.quit()

    def test_start_execution(self):
        self.driver.find_element_by_id("TCC-btn_start_TD-creating0").click()
        leave_queue = self.driver.find_element_by_id("TCC-btn_leave_queue_TD-wating0").text
        self.assertEqual("LEAVE QUEUE", leave_queue)
        self.driver.quit()

    def test_Leave_Queue(self):
        self.driver.find_element_by_id("TCC-btn_leave_queue_TD-wating0").click()
        start_btn = self.driver.find_element_by_id("TCC-btn_start_TD-creating0").text
        self.assertEqual("START", start_btn)
        self.driver.quit()

    def test_archived_tests(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar-menuitem_1"]').click()
        archived_tests = self.driver.find_element_by_id("AT-title").text
        self.assertEqual("Archived Tests", archived_tests)
        self.driver.quit()

    def test_scenario_library(self):
        self.driver.find_element_by_xpath('//*[@id="sidebar-menuitem_2"]').click()
        scenario_library = self.driver.find_element_by_xpath('//*[@id="app"]/div[6]/main/div/div[1]/div/div/div/div/span').text
        self.assertEqual("Scenario Library", scenario_library)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[6]/main/div/div[1]/div/div/div/div/div[1]/div[1]/button')
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
