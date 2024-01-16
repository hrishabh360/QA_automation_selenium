from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
import time
import pdb

# driver = webdriver.Chrome()
# driver = webdriver.Firefox()
webdriver_path = 'C:\edgedriver_win64\msedgedriver.exe'
ser = Service(webdriver_path)
driver = webdriver.Edge(service=ser)
driver.maximize_window()
url = 'http://demostore.supersqa.com/'

driver.get(url)



try:
    # Perform your actions here
    #By ID

    cart = driver.find_element(By.ID, "site-header-cart")
    print("cart:", cart, "\n")
    print("type of cart: ", type(cart), "\n")
    cart_txt = cart.text
    print(cart_txt)

    search_field = driver.find_element(By.ID, "woocommerce-product-search-field-0")
    search_field.send_keys('Hoodie')
    search_field.send_keys(Keys.ENTER)


    # #By.CSS_SELECTOR
    # my_acc = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9')
    my_acc = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]')
    # my_acc.click()

    pdb.set_trace()
    # Add a placeholder loop to keep the script running
    while True:
        time.sleep(40)  # Adjust the sleep duration as needed

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the WebDriver when you're ready to exit
    driver.quit() #will close everything > multiple tabs/browsers
    # driver.close() #will only close active browser
