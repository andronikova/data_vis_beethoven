from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
import lxml
import json
import numpy as np


url = "https://imslp.org/wiki/List_of_works_by_Ludwig_van_Beethoven"

page = requests.get(url).text


# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
#
# print(re.findall('Afghanistan', html))


html = BeautifulSoup(page,"lxml")

# print(html)
# with open("scrap_output.txt", "w", encoding="utf-8") as text_file:
#     text_file.write(str(html))

gdp_table = html.find("table", attrs={"class": "wikitable sortable"})
gdp_table_data = gdp_table.find_all("tr")


# print(len(gdp_table_data))

# with open("scrap_output.txt", "w", encoding="utf-8") as text_file:
#     text_file.write(str(gdp_table_data))



# info = []
with open("scrap_output.csv", "w", encoding="utf-8") as text_file:
    text_file.write('Op., WoO, Hess, Biamonti, Title, Key, Date, Scoring, Genre, Comments\n')
    for tr in gdp_table_data:
    #     # print('-----')
        line=""
        for td in tr.find_all("td"):
            if ('—' in td.text) or (len(td.text.strip())==0):
                line += ', ' + 'NaN'
            else:
                line += ', ' + td.text.rstrip().replace(',',' ').replace('♯',' sharp').replace('♭',' flat')

        line+= '\n'

        # print(line)
        text_file.write(line[2:])
        # info_1.append(td.text)

    # info.append(info_1)


# #  read only country name and number of regions and save it in json
# json_db = {}
# for country in info:
#     name = country[0].replace(u'\xa0', u' ')
#
#     if len(country) >= 2:
#         if len(country[1].split()) >= 1:
#             json_db[name[1:-1]] = country[1].split()[0]
#
#
# # print(json_db)
#
# # save json in file
# with open ('countrie_regions.json','w') as json_file:
#     json.dump(json_db, json_file, indent = 6)