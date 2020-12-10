from selenium import webdriver
import time

# executable_path should be specified with corresponding WebDriver path
driver_path = r'/Users/xxpal/Studio/Selenium/WebDriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

# Open browser with specified URL
url = r'https://www.baidu.com'
driver.get(url)

# Wait to ensure the webpage fully loaded
time.sleep(3)

# Find elements by ID, then, input some words for searching
driver.find_element_by_id('kw').send_keys('项目管理')
driver.find_element_by_id('su').click()

# Wait to ensure the searching results page fully loaded
time.sleep(3)

# Try to find specified link by text and then click it
driver.find_element_by_link_text('项目管理 - MBA智库百科').click()
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.quit()
