from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
webdriver_path = 'C:\edgedriver_win64\msedgedriver.exe'
ser = Service(webdriver_path)
driver = webdriver.Edge(service=ser)
driver.maximize_window()
url = 'https://www.python.org/'

driver.get(url)

cur_title = driver.title
expected_title = 'Welcome to Python.org'

if cur_title != expected_title:
    raise Exception("Went to python.org but got wrong title. Current title: {}".format(cur_title))

pypi_header_link_locator = '#top > nav > ul > li.pypi-meta > a'
pypi_header_link_elm = driver.find_element(By.CSS_SELECTOR, pypi_header_link_locator)
pypi_header_link_elm.click()

cur_url = driver.current_url
expected_url = 'https://pypi.org/'
assert cur_url == expected_url, f"Clicked on PyPi but the url opened was: {cur_url}"
print("PASS")

