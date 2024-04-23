#!/usr/bin/env python

import time

import wait
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

driver.find_element(By.XPATH,'//*[@id="stateArea"]/div[2]/div[1]/div/div[2]/button').click()

wait =10
print(str(wait) + '동안 기다립니다.')
time.sleep(wait)

driver.find_element(By.XPATH,'//*[@id="presentSearchMobile"]').click()

wait =10
print(str(wait) + '동안 기다립니다.')
time.sleep(wait)

def get_district_code(district_name):
    district_name = district_name.strip()  # 입력된 문자열의 양쪽 공백 제거

    if district_name == "종로구":
        return 2
    elif district_name == "중구":
        return 20
    elif district_name == "용산구":
        return 36
    elif district_name == "성동구":
        return 53
    else:
        return None  # 입력된 구가 없는 경우 None 반환
# 사용자로부터 구 이름 입력 받기
district_input = input("구 이름을 입력하세요: ")
# 입력된 구 이름에 따라 코드 가져오기
a = get_district_code(district_input)

if a is not None:
    xpath = f'//*[@id="table2"]/tbody/tr[{a}]/td[1]/span/a'
    driver.find_element(By.XPATH, xpath).click()
else:
    print("유효한 구 이름을 입력하세요.")

wait = 10
driver.implicitly_wait(wait)

driver.quit()
print('Browser Exit~!!')