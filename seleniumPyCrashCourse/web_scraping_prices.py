from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

webdriver_path = 'C:\edgedriver_win64\msedgedriver.exe'
ser = Service(webdriver_path)
driver = webdriver.Edge(service=ser)
driver.maximize_window()
driver.implicitly_wait(5)
url = 'http://demostore.supersqa.com/'
driver.get(url)


all_products = driver.find_elements(By.CLASS_NAME, 'product-type-simple')
# all_products = driver.find_elements(By.CLASS_NAME, 'product')
print(f"Number of Products: {len(all_products)}")


all_product_and_price = []
for product in all_products:
    price_element = product.find_element(By.CSS_SELECTOR, 'span.amount')
    price = price_element.text

    name_elm = product.find_element(By.CSS_SELECTOR, 'h2.woocommerce-loop-product__title')
    name = name_elm.text
    # print(name, ": ", price)
    all_product_and_price.append({'name': name, 'price' : price })

print(len(all_product_and_price))
print(all_product_and_price)
