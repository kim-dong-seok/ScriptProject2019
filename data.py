import requests
data= requests.get("https://api.bf4stats.com/api/playerInfo?plat=pc&name=sharqia&opt=dogtags&output=json").json()

data1=data["dogtags"]

for i in data1:
    print(i)