import requests
import json
from bs4 import BeautifulSoup

url = "https://tibia.fandom.com/wiki/Item_IDs"
response = requests.get(url)
soup = BeautifulSoup(response.text,"html.parser")
table_elements = soup.find_all("table",{"class": "wikitable"})
items = []
for table in table_elements:
    tr_elements = table.find_next("tbody").find_all("tr")
    for tr in tr_elements:
        datos = tr.find_all("td")
        if len(datos) > 0:
            print(datos[0])
            try:
                item_id = int(datos[1].text.split(",")[0])
                item_name = datos[0].text
            except:
                item_id = 0
                item_name = ""
            item={
                "id":item_id,
                "name":item_name,
            }
            items.append(item)

json_string = json.dumps(items)
with open("items.json","w") as file:
    file.write(json_string)
