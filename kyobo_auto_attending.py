import os
from time import sleep
import chromedriver_autoinstaller

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# pip install bs4
# pip install selenium
# pip install chromedriver_autoinstaller

print('교보문고 자동 출석 프로그램')
kyobo_id = 'rmswn96'
kyobo_pw = 'tomato119'

browser = None
sleep_time = 2

service = Service('/Users/seoha/Documents/workspace/workspace_crawling/drivers/chromedriver')
browser = webdriver.Chrome(service=service)

# 로그인
try:
    browser.get('http://www.kyobobook.co.kr')
    sleep(sleep_time)

    browser.find_element(By.CSS_SELECTOR, "#gnbLoginInfoList > li:first-child").click()
    sleep(sleep_time)

    browser.find_element(By.ID, "memid").send_keys(kyobo_id)
    browser.find_element(By.ID, "pw").send_keys(kyobo_pw)
    sleep(sleep_time)

    browser.find_element(By.CLASS_NAME, "btn_submit").click()
    sleep(sleep_time)
    print('로그인')
except Exception as e:
    print('로그인 에러')

# 출석체크
try:
    browser.find_element(By.CSS_SELECTOR, "#gnbLoginInfoList > li:nth-child(3)").click()
    sleep(sleep_time)
except Exception as e:
    print('출석 체크 클릭 에러')

# 첫 출석 시 alert -> enter
try:
    browser.switch_to.alert.accept()
    print('출석 체크')
except Exception as e:
    print('출석 체크 에러')

sleep(sleep_time)

# 문장수집
try:
    browser.find_element(By.ID, 'choice2').click()
    sleep(sleep_time)

    browser.find_element(By.CLASS_NAME, 'btn_stamp_check').click()
    sleep(sleep_time)

    browser.switch_to.alert.accept()
    print('문장수집')
except Exception as e:
    print('문장수집 에러')

sleep(sleep_time)

# 현재 출석 일수
try:
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, 'html.parser')
    ul = soup.select('.daily_stamp_list')
    checked_day = ul[0].select('.on')+ul[0].select('.complete')
    days = [day.text for day in checked_day]
    print(f'출석 일수 : {len(days)}일')
except Exception as e:
    print('출석 일수 에러')
