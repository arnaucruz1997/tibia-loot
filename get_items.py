import requests
import json
from bs4 import BeautifulSoup

class Items:
    def __init__(self, nameOutputFile, monsterNames):
        self.itemsdb = json.load(open("items.json"))
        self.itemsToLoot=[]
        self.nameOutputFile = nameOutputFile
        self.urls = self.get_url_from_monster_names(monsterNames)
        for url in self.urls:
            self.get_monster_item_list_from_url(url)
        self.transform_item_names_to_json()
    
    def get_url_from_monster_names(self, monsterNames):
        urls = []
        for monsterName in monsterNames:
            for word in monsterName.split():
                word.lower()
                word.capitalize()
                monsterName = monsterName.replace(word, word.capitalize())
            monsterName = monsterName.replace(" ","_")
            url = "https://tibia.fandom.com/wiki/"+monsterName.replace(" ","_")
            urls.append(url)
            print(url)
        return urls
    
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
monsterNames = ["Diabolic Imp", "Demon", "Demon Skeleton"]

items = Items(nameOutputFile, monsterNames)




