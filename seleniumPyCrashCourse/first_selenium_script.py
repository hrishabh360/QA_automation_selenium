'''
Author: Hrishabh
Date: Jan 16, 2024
'''

from selenium import webdriver
from selenium.webdriver.edge.service import Service

# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
webdriver_path = 'C:\edgedriver_win64\msedgedriver.exe'
ser = Service(webdriver_path)
driver = webdriver.Edge(service=ser)


driver.get('http://demostore.supersqa.com/')
print(driver.title)


'''
WebDriver provides several options of finding elements

find_element(BY..., <locator>)

By.ID
By.CSS_SELECTOR
By.XPATH
By.CLASS_NAME
By.LINK_TEXT
By.PARTIAL_LINK_TEXT
By.NAME
By.TAG_NAME
'''

'''
Selenium waits:
> implicit wait:
     driver = webdriver.Chrome()
     driver.implicitly_wait(10)
     > Checking the visibility of element for every half second until 10 sec before throwing element cant be found exception\
     
> explicit wait
    from selenium.webdriver.support import expected_conditions as EC
    driver = webdriver.Chrome()
    elm = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "username")))
'''

