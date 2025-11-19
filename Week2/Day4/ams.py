import datetime

class Airline():
    def __init__(self, name):
        self.id = id
        self.name = name 
        # self.planes = planes # list of airplanes belonging to an airline
        pass

class Airplane():
    def __init__(self, id, current_location, company, next_flights):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = next_flights
    
    def fly(self, destination):
        if destination in self.next_flights.values():
            print(f"plane: {self.id} taking off from {self.current_location}")
            self.current_location = destination
            print(f"plane: {self.id} just landed in {self.current_location}")
            return self.current_location
        else:
            return f"no flight scheduled for {destination}."
    
    def location_on_date(self, date):
            if date in self.next_flights.keys():
                self.current_location = self.next_flights[date]
                return f"plane: {self.id} will be at {self.next_flights[date]} on {date}"
            else:
                return f"No flight scheduled, plane: {self.id} will be at {self.current_location} on {date}"
        
    def avaliable_on_date(self, date, location):
        if date in self.next_flights.keys():
            return f"Plane: {self.id} can't fly on {date}, it already has a flight to {self.next_flights[date]}"
        else:
            return True

class Flight():
    def  __init__(self, date, destination):
        self.date = date
        self.destination = destination

    def __str__(self):
        return f"{self.date}, {self.destination}"

    def __repr__(self):
        return f"{self.date}, {self.destination}"


if __name__=="__main__":
    JFK = Airline("jfk")
    flight_1 = Flight(date=datetime.datetime(2025, 11, 12), destination="lax")
    flight_2 = Flight(date=datetime.datetime(2025, 11, 18), destination="lhr")
    flight_3 = Flight(date=datetime.datetime(2026, 1, 17), destination="hnd")
    airplane_1 = Airplane("01", "jfk", "delta", next_flights={flight_1.date: flight_1.destination, flight_2.date: flight_2.destination, flight_3.date: flight_3.destination})
    print(airplane_1.fly(destination="lax"))
    print(airplane_1.location_on_date(date=datetime.datetime(2025, 11, 18)))
    print(airplane_1.location_on_date(date=datetime.datetime(2027, 11, 18)))
    print(airplane_1.avaliable_on_date(date=datetime.datetime(2026, 1, 17), location="bgr"))