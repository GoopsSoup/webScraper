from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.get("https://trello.com/b/XyvHrkbi/voxlblade-remastered")

WebDriverWait(driver, 20).until(
    ec.presence_of_all_elements_located((By.CSS_SELECTOR, "span.kncNzJ_M0ejtxQ.color-blind-pattern-purple"))
)

cards = driver.find_elements(By.CSS_SELECTOR, "span.kncNzJ_M0ejtxQ.color-blind-pattern-purple")

for q in cards:
    print(q.text)

driver.quit()