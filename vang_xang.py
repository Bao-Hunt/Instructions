# thu thập dữ liệu và và xăng từ 2 trang web

import requests
from bs4 import BeautifulSoup
import json
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

# Đường dẫn đến trình điều khiển của trình duyệt (ví dụ: chromedriver)
driver_path = '/usr/bin/chromedriver'

# URL của các trang web cần crawl
url_sjc = 'https://sjc.com.vn/'
url_pvoil = 'https://www.pvoil.com.vn/truyen-thong/tin-gia-xang-dau'

# Khởi tạo dịch vụ ChromeDriver
service = Service(driver_path)

data = {}

# Crawl dữ liệu từ sjc.com.vn
try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(url_sjc)

    wait = WebDriverWait(driver, 10)
    table = wait.until(EC.presence_of_element_located((By.XPATH, '//table[@class="table scroll"]/tbody')))
    time.sleep(5)

    table_html = table.get_attribute('outerHTML')
    soup = BeautifulSoup(table_html, 'html.parser')
    rows = soup.find_all('tr')
    
    sjc_data = []

    for row in rows:
        cell = row.find_all('td')
        
        if len(cell) >= 3:
            loai = cell[0].text.strip()
            mua = cell[1].text.strip()
            ban = cell[2].text.strip()
        else:
            continue
        sjc_data.append({
            'LOẠI VÀNG': loai,
            'MUA VÀO': mua,
            'BÁN RA': ban
        })
    sjc_data.pop(0)
    data['sjc'] = sjc_data
    
except TimeoutException:
    print('Timeout while waiting for the table to load on sjc.com.vn')
except WebDriverException as e:
    print(f'WebDriver error on sjc.com.vn: {e}')
finally:
    driver.quit()

# Crawl dữ liệu từ pvoil.com.vn
try:
    with requests.get(url_pvoil) as response:
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        tables = soup.find_all('table', class_='table')
        
        if tables:
            table = tables[0]
            tr = table.find_all('tr')
            tr.pop(0)
            pvoil_data = []
            
            for row in tr:
                td = row.find_all('td')
                if len(td) >= 4:
                    loai_xang = td[1].text.strip()
                    gia_ban = td[2].text.strip()
                    pvoil_data.append({
                        'LOẠI_XĂNG': loai_xang,
                        'GIÁ_BÁN': gia_ban
                    })
            data['pvoil'] = pvoil_data
        else:
            print('Không tìm thấy bảng dữ liệu trên pvoil.com.vn')
except requests.RequestException as e:
    print(f'Không thể truy cập trang web pvoil.com.vn: {e}')

# Lưu dữ liệu vào file JSON
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print('Dữ liệu đã được lưu vào file data.json')
