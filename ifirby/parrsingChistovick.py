import requests
from bs4 import BeautifulSoup
import csv
from pandas import DataFrame

url = 'https://cheapkeys.ovh/table.php'

r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')
g = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')

set = []
name = []
baty131shop = []
gamestorfarm = []
steamkeystore = []
cards = []
price = []
reit = []
best_price = []

for o in range(len(g)):
    # set.append(soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find_all('a', target='_blank')[0].text)
    # name.append(soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find_all('a', target='_blank')[1].text)
    strbaty131shop = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find(attrs={"data-clipboard-text": "summersale1"})
    if strbaty131shop != None:
        baty131shop.append(strbaty131shop.text)
    elif strbaty131shop == None:
        baty131shop.append('None')

    strgamestorfarm = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find(attrs={"data-clipboard-text": "5procent5"})
    if strgamestorfarm != None:
        gamestorfarm.append(strgamestorfarm.text)
    elif strgamestorfarm == None:
        gamestorfarm.append('None')

    strsteamkeystore1 = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find(attrs={"data-clipboard-text": "Proxzy"})
    # strsteamkeystore2 = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find('a', attrs={"data-clipboard-text": "None"})
    strsteamkeystore3 = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find(attrs={"data-clipboard-text": "OVH12"})
    if strsteamkeystore1 != None:
        steamkeystore.append(strsteamkeystore1.text)
    # elif strsteamkeystore2 != None:
    #     steamkeystore.append(strsteamkeystore2.text)
    elif strsteamkeystore3 != None:
        steamkeystore.append(strsteamkeystore3.text)
    else:
        steamkeystore.append('None')
    if ((strsteamkeystore1 != None and strsteamkeystore3 != None and strgamestorfarm != None and strbaty131shop != None) and (strbaty131shop < strgamestorfarm and (strbaty131shop < strsteamkeystore1 or strbaty131shop < strsteamkeystore3))) or (strbaty131shop != None and strsteamkeystore1 == None and strsteamkeystore3 == None and strgamestorfarm == None):
        best_price.append(strbaty131shop.text)
    elif ((
                    strsteamkeystore1 != None and strsteamkeystore3 != None and strgamestorfarm != None and strbaty131shop != None) and (
                      strgamestorfarm < strbaty131shop and (
            strgamestorfarm < strsteamkeystore1 or strgamestorfarm < strsteamkeystore3))) or (
                strbaty131shop == None and strsteamkeystore1 == None and strsteamkeystore3 == None and strgamestorfarm != None):
        best_price.append(strgamestorfarm.text)
    elif ((
                    strsteamkeystore1 != None and strsteamkeystore3 == None and strgamestorfarm != None and strbaty131shop != None) and (
                      strsteamkeystore1 < strbaty131shop and strgamestorfarm > strsteamkeystore1)) or (
                strbaty131shop == None and strsteamkeystore1 != None and strsteamkeystore3 == None and strgamestorfarm == None):
        best_price.append(strsteamkeystore1.text)
    elif ((
                    strsteamkeystore1 == None and strsteamkeystore3 != None and strgamestorfarm != None and strbaty131shop != None) and (
                      strsteamkeystore3 < strbaty131shop and strsteamkeystore3 < strgamestorfarm )) or (
                strbaty131shop == None and strsteamkeystore1 == None and strsteamkeystore3 != None and strgamestorfarm == None):
        best_price.append(strsteamkeystore3.text)
    else:
        best_price.append('None')
print(best_price)
# print(g)
# if g == True:
#     print("yes")
# elif g == False:
#     print('noonon')
# elif g == None:
#     print('none')
#

#
# a = g.find(attrs={"data-clipboard-text": "5procent5"}).text
# lst = list(map(lambda target: target.text, g))
# for i in range(len(lst)):
#     print(lst[i]+' |')
#
