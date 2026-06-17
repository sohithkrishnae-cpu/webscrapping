import requests
from bs4 import BeautifulSoup

# website link to scrape news from:
base_url = "https://capital.com/lp-trade-tech-stocks-eu?utm_medium=cpc&utm_source=microsoft&utm_campaign=web_fca_search_microsoft_uk_en_troas_ftd_ua&utm_term=stock%20trading%20platforms&adgroupid=1337008686846694&matchtype=p&creative=&device=c&loc_physical=162592&msclkid=60f310ee3bf8142ef6777ac4f77e6014&utm_content=UK_EN_Search_Stocks-Platform_NA_Phrase" # add stock name at the end e.g. apple

headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(base_url, headers=headers)
soup = BeautifulSoup(res.text, 'lxml')

# names of the most advance stocks:
stock_name = soup.select(".stringEllipsed") # 
stock_name_list = []
stock_change_list = []
even = 0

for i in stock_name:
    if even % 2 == 0:
        stock_name_list.append(i.text)
    even += 1

print(stock_name_list)

#one_day_change = soup.select(".grow") #
#print(one_day_change)
rows = soup.select("tr.textRight")
for row in rows:
    symbol = soup.select_one("tr.textRight")
    stock_change_list.append(symbol)
print(stock_change_list)