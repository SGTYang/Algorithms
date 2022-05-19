class UndergroundSystem:

    def __init__(self):
        self.checkin_db = {}
        self.checkout_db = {}
        
    def checkIn(self, id_: int, stationName: str, t: int) -> None:
        self.checkin_db[id_] = (stationName, t)

    def checkOut(self, id_: int, stationName: str, t: int) -> None:
        checkin_station, checkin_time = self.checkin_db[id_]
        
        route = (checkin_station, stationName)
        if not self.checkout_db.get(route):
            self.checkout_db[route] = [0, 0]
            
        self.checkout_db[route][0] += (t - checkin_time)
        self.checkout_db[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        time, freq = self.checkout_db[route]
        return time / freq
    
