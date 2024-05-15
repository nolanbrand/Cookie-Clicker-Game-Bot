from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

keep_clicking = True
start = time.time()
game_start_time = time.time()
while keep_clicking:
    cookie.click()
    end = time.time()

    if end - start > 5:
        money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
        items_name_cost = driver.find_elements(By.CSS_SELECTOR, value="#store b")

        item_dict = {
            items_name_cost[i].text.split("-")[0].strip()
            : int(items_name_cost[i].text.split("-")[1].strip().replace(",", ""))
            for i in range(len(items_name_cost) - 1)
        }

        for key in item_dict:
            item_cost = 0
            if money > item_dict[key] > item_cost:
                item_cost = item_dict[key]
                item = key
        purchase_item = driver.find_element(By.ID, value=f"buy{item}")
        purchase_item.click()

        start = time.time()

    if end - game_start_time > 300:
        cookies_rate = driver.find_element(By.ID, value="cps")
        print(cookies_rate.text)
        keep_clicking = False
