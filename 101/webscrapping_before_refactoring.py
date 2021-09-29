import json
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

url = "https://www.nba.com/stats/players/traditional/?PerMode=Totals&dir=-1&Season=2019-20&SeasonType=Regular%20Season"

# 1. Connecting to the NBA website
option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)

driver.get(url)
driver.implicitly_wait(10)

# 2. Accepting thrust message
driver.find_element_by_id('onetrust-accept-btn-handler').click()
time.sleep(1)

# 3. Selecting the target stats
driver.find_element_by_xpath(f"//th[@data-field='FG3M']").click()
driver.implicitly_wait(10)

element = driver.find_element_by_xpath(f"//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

# 4. Parsing HTML content
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# 5. Structuring data with pandas
df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', '3PM']]
df.columns = ['pos', 'player', 'team', 'total']

# 6. Transforming data targets in dictionaries
top10ranking = {'3points': df.to_dict('records')}
driver.quit()

# 7. Convert e store data on JSON file
js = json.dumps(top10ranking)
fp = open('nba_ranking.json', 'w')
fp.write(js)
fp.close()






