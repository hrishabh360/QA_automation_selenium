from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)

webdriver_path = 'C:\edgedriver_win64\msedgedriver.exe'
ser = Service(webdriver_path, options = options)
driver = webdriver.Edge(service=ser)
driver.maximize_window()
url = 'https://www.python.org/'


driver.get(url)

cur_title = driver.title
expected_title = 'Welcome to Python.org'
driver.implicitly_wait(10)

if cur_title != expected_title:
    raise Exception("Went to python.org but got wrong title. Current title: {}".format(cur_title))


search_field_id = 'id-search-field'
search_field_element = driver.find_element(By.ID, search_field_id)
search_field_element.send_keys("testing")

go_btn_id = 'submit'
go_btn_element = driver.find_element(By.ID, go_btn_id)
go_btn_element.click()

first_result_element_xpath = '//*[@id="content"]/div/section/form/ul/li[1]'
first_result_element = driver.find_element(By.XPATH, first_result_element_xpath)
import pdb


pdb.set_trace()

# assert first_result_element.is_displayed(), f'The result is not displayed'

# OR

if first_result_element.is_displayed():
    print('PASS')
else:
    raise Exception(f'The result is not displayed')

# driver.quit()