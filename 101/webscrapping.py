import json
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(name)s %(levelname)s %(message)s',
    filename='webscrapping.log',
    filemode='w'
    )

url = "https://www.nba.com/stats/players/traditional/?PerMode=Totals&dir=-1&Season=2019-20&SeasonType=Regular%20Season"

rankings = {
    '3points': {'field': 'FG3M', 'label': '3PM'},
    'points': {'field': 'PTS', 'label': 'PTS'},
    'assistants': {'field': 'AST', 'label': 'AST'},
    'rebounds': {'field': 'REB', 'label': 'REB'},
    'steals': {'field': 'STL', 'label': 'STL'},
    'blocks': {'field': 'BLK', 'label': 'BLK'},
}


def buildrank(type):
    field = rankings[type]['field']
    label = rankings[type]['label']
    driver.find_element_by_xpath(f"//th[@data-field='{field}']").click()
    logging.debug(f"NBA stats for {field} selected")
    driver.implicitly_wait(10)
    element = driver.find_element_by_xpath(f"//div[@class='nba-stat-table']//table")
    html_content = element.get_attribute('outerHTML')
    logging.debug(f"HTML data for {field} selected")
    soup = BeautifulSoup(html_content, 'html.parser')
    logging.debug(f"HTML data for {field} parsed")
    table = soup.find(name='table')
    logging.debug(f"HTML data for {field} converted to table")
    df_full = pd.read_html(str(table))[0].head(10)
    logging.debug(f"HTML data for {field} converted to data frame")
    df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', label]]
    df.columns = ['pos', 'player', 'team', 'total']
    logging.debug(f"Data frame columns for {field} selected")
    return df.to_dict('records')


option = Options()
option.headless = True
driver = webdriver.Firefox(options=option)
logging.debug("Firefox initialized.")

driver.get(url)
logging.debug("URL oppened")

driver.implicitly_wait(10)

driver.find_element_by_id('onetrust-accept-btn-handler').click()
logging.debug("One Trust Accepted")
time.sleep(1)

top10ranking = {}
for k in rankings:
    top10ranking[k] = buildrank(k)
    logging.debug(f"Rank builded for {k}.")

driver.quit()
logging.debug("Firefox closed")

js = json.dumps(top10ranking, indent=4, sort_keys=True)
logging.debug("JSON file builded")
fp = open('nba_ranking.json', 'w')
fp.write(js)
logging.debug("JSON file written")
fp.close()
