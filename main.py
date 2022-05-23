from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

import subprocess
import chromedriver_autoinstaller
import time
import collections
import csv

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

try:
    # 디버거 크롬 구동
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp1"')
except:
    # 디버거 크롬 구동
    subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp1"')
option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
except:
    chromedriver_autoinstaller.install('./')
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
driver.implicitly_wait(20)

driver.get('https://www.starbucks.co.kr/store/store_map.do')
starbucks = []
search = driver.find_element_by_link_text('지역 검색')
time.sleep(1)
search.click()

time.sleep(1)
# 개발자도구로 class : set_sido_cd_btn의 데이터 긁어옴
search = driver.find_elements_by_class_name('set_sido_cd_btn')

for item in search:
    item.click()
    time.sleep(1)

    # data-sidocd='01~17' 서울~세종
    if '17' == item.get_attribute('data-sidocd'):
        # 소스 가져오기
        src = driver.page_source

        # BeautifulSoup 객체로 변환
        soup = BeautifulSoup(src)
        name = soup.select('li[data-name]')
        for name_one in name:
            x = name_one['data-lat'] # 위도 저장
            y = name_one['data-long'] # 경도 저장
            z = name_one['data-name'] # 지점명 저장
            p = name_one.select_one('p').text.split('1522-3232')[0] # 한국 스타벅스는 번호가 전부 동일해 동일 Parameter 사용
            starbucks.append({'name': z, 'address': p, 'lat': x, 'long':y}) # dict 형태로 리스트에 저장
        time.sleep(1)

        # 열린 페이지 닫기
        driver.close()
    else:
        search2 = driver.find_element_by_link_text('전체')
        search2.click()
        driver.implicitly_wait(5)
        time.sleep(1)

        src = driver.page_source

        soup = BeautifulSoup(src)
        name = soup.select('li[data-name]')
        for name_one in name:
            x = name_one['data-lat']
            y = name_one['data-long']
            z = name_one['data-name']
            p = name_one.select_one('p').text.split('1522-3232')[0]
            starbucks.append({'name': z, 'address': p, 'lat': x, 'long':y})
        time.sleep(1)

        # 지역검색값으로 되돌아감
        search3 = driver.find_element_by_link_text('지역 검색')
        search3.click()
        time.sleep(1)

# 리스트 중복값 제거
starbucks = list(map(dict, collections.OrderedDict.fromkeys(tuple(sorted(d.items())) for d in starbucks)))

with open('starbucks.csv', 'w', newline='') as f:
    fieldnames =['지점명', '주소', '위도', '경도']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for i in starbucks:
        writer.writerow({'지점명': i['name'], '주소': i['address'], '위도': i['lat'], '경도': i['long']})
