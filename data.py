import requests
online = requests.get("https://api.bf4stats.com/api/playerInfo?plat=pc&name=sharqia&output=json").json()

print(online["player"])
for i in online:
    print(i)