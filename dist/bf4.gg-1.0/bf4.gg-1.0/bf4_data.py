import requests
import bf4
class player_data:
    def __init__(self,player_name=" ",player_plat=" "):
        self.data = requests.get(bf4.playerInfo(player_plat,player_name)).json()
        self.player = self.data["player"]
        self.stats =self.data["stats"]
        self.dogtags =self.data["dogtags"]
        self.weapons = self.data["weapons"]
        self.weaponCategory = self.data["weaponCategory"]
        self.kititems = self.data["kititems"]
        self.vehicles = self.data["vehicles"]
        self.modes = self.stats["modes"]
        self.kits = self.stats["kits"]
        self.vehicleCategory =self.data["vehicleCategory"]
        self.awards = self.data["awards"]
        self.assignments = self.data["assignments"]
        self.upcomingUnlocks = self.data["upcomingUnlocks"]
        self.rank_weapons = sorted(self.weapons, key=lambda t: t["stat"]["kills"], reverse=True)
        self.rank_vehicles = sorted(self.vehicles, key=lambda t: t["stat"]["kills"], reverse=True)
        self.rank_modes = sorted(self.modes, key=lambda t: t["score"], reverse=True)

        self.ranking = requests.get(bf4.playerRankings(player_plat,player_name)).json()
        self.player_ranking = self.ranking["rankings"]
        for i in range(len(self.player_ranking)):
            if self.player_ranking[i]["rank"] == None:
                self.player_ranking[i]["rank"] = 100000
        self.sort_ranking = sorted(self.player_ranking, key=lambda t: t["rank"])
        for i in range(len(self.player_ranking)):
            if self.player_ranking[i]["rank"] == 100000:
                self.player_ranking[i]["rank"] = 0
        self.sort_ranking1=self.sort_ranking[0]
        self.sort_ranking2 = self.sort_ranking[1]
        self.sort_ranking3 = self.sort_ranking[2]

        self.ranking1=[]
        self.ranking2 = []
        self.ranking3 = []
        self.ranking4 = []
        for i in self.player_ranking:
            if i["rank"] == None:
                i["rank"] = 0
            if i["count"] == None:
                i["count"] = 0
            if i["value"] == None:
                i["value"] = 0
            if i["group"] == "player":
                self.ranking1.append(i)
            elif i["group"] == "kit":
                self.ranking2.append(i)
            elif i["group"] == "mode":
                self.ranking3.append(i)
            elif i["group"] == "kititem":
                self.ranking4.append(i)