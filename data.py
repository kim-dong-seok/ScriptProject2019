import requests
online = requests.get("https://api.bf4stats.com/api/onlinePlayers?output=json").json()

print(online)
for i in online:
    print(i)