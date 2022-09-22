class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}
        self.routeTime = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        depart = self.checkInMap.pop(id)
        route = f'{depart[0]}-{stationName}'
        if route in self.routeTime:
            prev = self.routeTime[route]
            self.routeTime[route] = (prev[0] + t - depart[1], prev[1] + 1)
        else:
            self.routeTime[route] = (t - depart[1], 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = f'{startStation}-{endStation}'
        return self.routeTime[route][0] / self.routeTime[route][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)