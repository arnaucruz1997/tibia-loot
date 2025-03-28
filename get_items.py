import requests
import json
from bs4 import BeautifulSoup

class Items:
    def __init__(self, nameOutputFile, urls):
        self.itemsdb = json.load(open("items.json"))
        self.itemsToLoot=[]
        self.nameOutputFile = nameOutputFile
        self.urls = urls
        for url in urls:
            self.get_monster_item_list_from_url(url)
        self.transform_item_names_to_json()

    def get_monster_item_list_from_url(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text,"html.parser")
        table_elements = soup.find_all("div",{"class": "loot-table"})

        li_elements = table_elements[0].find_all("li")
        for li in li_elements:
            if li.find("a") is not None:
                if li.find("a").text not in self.itemsToLoot:
                    self.itemsToLoot.append(li.find("a").text)

    def transform_item_names_to_json(self):
        res = []
        for item in self.itemsdb:
            for itemToLoot in self.itemsToLoot:
                if item["name"].lower().replace(" ","") == itemToLoot.lower().replace(" ",""):
                    res.append({
                        "count":1,
                        "id":item["id"],
                    })
        json_string = json.dumps(res)
        with open("./outputs/"+nameOutputFile,"w") as file:
            file.write(json_string)
        
nameOutputFile = "goroma_volcan.json"
urls = [
    "https://tibia.fandom.com/wiki/Diabolic_Imp",
    "https://tibia.fandom.com/wiki/Hellfire_Fighter",
    "https://tibia.fandom.com/wiki/Demon",
    "https://tibia.fandom.com/wiki/Dragon_Lord",
    "https://tibia.fandom.com/wiki/Dragon_Lord_Hatchling",
]

items = Items(nameOutputFile, urls)




