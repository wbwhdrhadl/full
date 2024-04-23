#!/usr/bin/env python

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
print(type(driver))
print('-' * 50)

print('Go Google~!!')
url = 'https://golmok.seoul.go.kr/stateArea.do'
driver.get(url)
# 버튼을 식별하고 클릭하기
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "store")))
button.click()

wait = 3
print(str(wait) + '동안 기다립니다.')
time.sleep(wait)

wait = 3
driver.implicitly_wait(wait)

driver.quit()
print('Browser Exit~!!')