from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'))
URL = 'https://www.amazon.com/dp/B09RWVV3XZ/?coliid=I1QWBI4L5MS2CJ&colid=2HCWJ1E022ZH&ref_=lv_ov_lig_dp_it&th=1'
driver.get(URL)
# time.sleep(1)

soup = BeautifulSoup(driver.page_source, "html.parser")

title = soup.select_one("span[id='productTitle']").text
price = soup.select_one("span[class='a-offscreen']").text


print(title)
print(price)

driver.close()