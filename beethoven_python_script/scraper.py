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
with open("../scrap_output.csv", "w", encoding="utf-8") as text_file:
    text_file.write('Op.,WoO,Hess,Biamonti,Title,Key,Date,Scoring,Genre,Comments\n')
    for tr in gdp_table_data:
    #     # print('-----')
    #     print()
    #     print(tr)
        line=""
        for td in tr.find_all("td"):

            td_text = td.text.strip()
            if len(td_text)==0:
                line += ', ' + 'NaN'
            else:
                line += ', ' + td_text.replace(',',' ').replace('♯',' sharp').replace('♭',' flat').lstrip('0')


        line += '\n'

        # print(line)
        text_file.write(line[2:])

