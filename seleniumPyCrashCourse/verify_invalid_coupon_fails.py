from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
from selenium.common.exceptions import NoSuchElementException
def open_browser():
    webdriver_path = 'C:\edgedriver_win64\msedgedriver.exe'
    ser = Service(webdriver_path)
    driver = webdriver.Edge(service=ser)
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def go_to_home_page():
    url = 'http://demostore.supersqa.com/'
    driver.get(url)

def add_first_item_to_cart(driver):
    first_add_btn = driver.find_element(By.CLASS_NAME, 'add_to_cart_button')
    first_add_btn.click()

def go_to_cart_page(driver):
    cart_page = 'http://demostore.supersqa.com/cart/'
    driver.get(cart_page)

def apply_coupon(driver, coupon_code):
    coupon_field = driver.find_element(By.ID, 'coupon_code')
    coupon_field.send_keys(coupon_code)
    apply_btn = driver.find_element(By.CSS_SELECTOR, '#post-7 > div > div > form > table > tbody > tr:nth-child(2) > td > div > button')
    apply_btn.click()

def verify_cart_has_item(driver):
    for i in range(5):
        try:
            driver.find_element(By.CLASS_NAME, 'cart_item')
            return
        except NoSuchElementException:
            print("Item not in cart, Retry After 2 Seconds")
            time.sleep(2)
            driver.refresh()

def get_displayed_error_message(driver):
    return driver.find_element(By.XPATH, '//*[@id="post-7"]/div/div/div[1]/ul').text




if __name__ == '__main__':
    driver = open_browser()
    go_to_home_page()
    add_first_item_to_cart(driver)
    go_to_cart_page(driver)
    verify_cart_has_item(driver)
    apply_coupon(driver, 'fakeone')
    get_displayed_error_message(driver)
    err_msg = get_displayed_error_message(driver)
    exp_msg = 'Coupon "fakeone" does not exist!'
    assert err_msg == exp_msg, f"Unexpected Err message: {err_msg}"
    print('PASS')
    time.sleep(40)
    driver.quit()