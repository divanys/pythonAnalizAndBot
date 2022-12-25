import requests
from bs4 import BeautifulSoup
import csv
from pandas import DataFrame

url = 'https://cheapkeys.ovh/table.php'

r = requests.get(url).text
soup = BeautifulSoup(r, 'lxml')
g = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[0].find('a', dadaa_nrnrnr='dsdsd')
print(g)
if g == True:
    print("yes")
elif g == False:
    print('noonon')
elif g == None:
    print('none')
# a = g.find(attrs={"data-clipboard-text": "5procent5"}).text
#
# print(a)
# s = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[0].find('a', class_="href").next_element.text
# print(s)
# lst = list(map(lambda target: target.text, g))
# for i in range(len(lst)):
#     print(lst[i]+' |')
# ksnsds = []
# a = []
# for i in range(len(g)):
#     a.append(soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row'))
#     for j in range(len(a)):
#         ksnsds.append(a[i].find_all('a', target='_blank')[j].text)
# print(ksnsds)


# [0].find('a', data_clipboard_text_='summersale1')
# print(g)
# print(s)
# print(type(g))
#         ("set", "name", "best price", "baty131shop", "gamestorfarm", "steamkeystore", "cards", "price", "reit")
# with open('data.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         ('set')
#    )
# lst = list(map(lambda target: target.text, g))
# for i in range(len(lst)):
#     print(lst[i])
#
set = []
name = []
best_price = []
baty131shop = []
gamestorfarm = []
steamkeystore = []
cards = []
price = []
reit = []

# print('g ', len(g))
# for o in range(len(g)):
#     # print('o ', o)
#     set.append(soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find('a', target='_blank').text)
#
# resNone = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find('tr', class_='row').find('a', data_clipboard_text="5procent5")
# print(resNone)
# for o in range(len(g)):
#     # set.append(soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find_all('a', target='_blank')[0].text)
#     # name.append(soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find_all('a', target='_blank')[1].text)
#     res = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find('a', class_="href", data_clipboard_text='summersale1')
#     if res == resNone:
#         baty131shop.append('0')
#     else:
#         baty131shop.append(res.text)
#
#     print(baty131shop)
# allCol = {'set': set, 'name': name}

# df = DataFrame(baty131shop, columns=['baty131shop'])
# ex_csv = df.to_csv(r'excsv3.csv')

# k = []
# print('g ', len(g))
# for o in range(len(g)):
#     # print('o ', o)
#     k.append(soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find('a', target='_blank').text)
# #
# dff = DataFrame(k, columns=['name'])
# with open('excsv.csv', 'a') as file:
#     ex_csv = dff.to_csv(r'excsv.csv')
# print(j)
# print('j ', j)
#
# for item in j:
#     with open("data.csv", "a") as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             item
#         )
# i = 0
# while i < 325:
#     try:
#         for o in range(len(g)):
#             res = soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[o].find('a', data_clipboard_text='summersale1').text
#             if res != None:
#                 baty131shop.append(soup.find('div', id='cards').find('table', class_="ttt").find('tbody').find_all('tr', class_='row')[i].find('a', data_clipboard_text='summersale1').text)
#             else:
#                 baty131shop.append('0')
#             i += 1
#             print('o ', o, 'lst ', baty131shop)
#     except:
#         i += 1
#         continue
#
# print(baty131shop)

#
# a = None
# if a == True:
#     print(a)


# a = 'dadaefaef'
#
# class NoneType:
#     a = NoneType
#
#
# if a == True:
#     print(a)


# import re
# for tag in soup.find_all(re.compile("^d")):
#     print(tag.name)

# g.find_all('a', attrs={"data-clipboard-text": "5procent5"})
