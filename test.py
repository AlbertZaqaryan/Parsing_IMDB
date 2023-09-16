from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import pandas as pd


options = Options()
options.add_argument("window-size=1920,1080")
ua = UserAgent()
user_agent = ua.random
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(options=options)
try:
    film_name_list = []
    film_date_list = []
    film_rating_list = []
    driver.get(url='https://www.imdb.com/chart/top/?ref_=nv_mv_250')
    for i in range(1, 251):
        film_name = driver.find_element(By.CSS_SELECTOR, f'#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) > div.ipc-metadata-list-summary-item__c > div > div > div.ipc-title.ipc-title--base.ipc-title--title.ipc-title-link-no-icon.ipc-title--on-textPrimary.sc-b51a3d33-7.huNpFl.cli-title > a > h3').text
        film_date = driver.find_element(By.CSS_SELECTOR, f'#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) > div.ipc-metadata-list-summary-item__c > div > div > div.sc-b51a3d33-5.ibuRZu.cli-title-metadata > span:nth-child(1)').text
        film_rating = driver.find_element(By.CSS_SELECTOR, f'#__next > main > div > div.ipc-page-content-container.ipc-page-content-container--center > section > div > div.ipc-page-grid.ipc-page-grid--bias-left > div > ul > li:nth-child({i}) > div.ipc-metadata-list-summary-item__c > div > div > span > div > span').text
        film_name_list.append(film_name)
        film_date_list.append(film_date)
        film_rating_list.append(film_rating[:3])
    time.sleep(3)
    data = pd.read_csv('new.csv')
    data['name'] = film_name_list
    data['date'] = film_date_list
    data['rating'] = film_rating_list
    data.to_csv('newdata.csv', index=False, index_label=False)
except Exception as ex:
    print(ex.__class__.__name__)
finally:
    driver.close()
    driver.quit()
