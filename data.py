import requests
data= requests.get("https://api.bf4stats.com/api/playerRankings?plat=pc&name=1ApRiL&output=json").json()

data1=data["rankings"]

for i in data1:
    print(i)