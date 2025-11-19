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
            return f"Plane: {self.id} can't fly on {date},to {location} it already has a flight to {self.next_flights[date]}"
        else:
            return True

class Flight():
    def  __init__(self, date, destination, origin):
        self.date = date
        self.destination = destination
        self.origin = origin

class Airport():
    def __init__(self, city, planes, scheduled_departures, scheduled_arrivals, total_flights=None):
        self.city = city
        self.planes = planes
        self.scheduled_departures = scheduled_departures
        self.schedule_arrivals = scheduled_arrivals
        self.total_flights = total_flights

    def schedule_flight(self, destination, datetime):
        for plane in self.planes:
            for departure in self.scheduled_departures.keys():
                if departure in plane.next_flights.keys():
                    if datetime in self.scheduled_departures.keys():
                        return f"No flights avaliable today"
                    else:
                        new_flight = Flight(date=datetime, destination=destination, origin=plane.current_location)
                        self.scheduled_departures[new_flight.date] = destination
                        print(f"New flight for plane: {plane.id} is scheduled for {destination} at {datetime}")
                        return self.scheduled_departures
              
    def info(self, start_date, end_date):
        self.total_flights = []
        for arrival in self.schedule_arrivals.keys():
                if arrival >= start_date and arrival <= end_date:
                    string_to_append = f"{arrival}, {self.schedule_arrivals[arrival]}"
                    self.total_flights.append(string_to_append)
                else:
                    continue
        for departure in self.scheduled_departures.keys():
                if departure >= start_date and departure <= end_date:
                    string_to_append = f"{departure}, {self.scheduled_departures[departure]}"
                    self.total_flights.append(string_to_append)
                else:
                    continue
        return f"The following flights are scheduled between the dates provided: {self.total_flights}"
    
    def __str__(self):
        return f"total flights: {self.total_flights}"

    def __repr__(self):
        return f"total flights: {self.total_flights}"


if __name__=="__main__":

    delta = Airline("delta")
    southwest = Airline("southwest")
    elal = Airline("elal")

    flight_1 = Flight(date=datetime.datetime(2028, 1, 1), destination="South Africa", origin="New York")
    flight_2 = Flight(date=datetime.datetime(2028, 1, 1), destination="Tel Aviv", origin="New York")
    flight_3 = Flight(date=datetime.datetime(2028, 1, 1), destination="Hong Kong", origin="New York")
    
    flight_4 = Flight(date=datetime.datetime(2026, 1, 1), destination="New York", origin="Japan")
    flight_5 = Flight(date=datetime.datetime(2028, 1, 1), destination="New York", origin="Italy")
    flight_6 = Flight(date=datetime.datetime(2025, 1, 1), destination="New York", origin="Morocco")

    airplane_1 = Airplane(id="01", current_location="New York", company=delta, next_flights={flight_1.date: flight_1.destination, flight_2.date: flight_2.destination, flight_3.date: flight_3.destination})
    airplane_2 = Airplane(id="02", current_location="New York", company=southwest, next_flights={flight_4.date: flight_4.destination, flight_5.date: flight_5.destination, flight_6.date: flight_6.destination})

    print(airplane_1.fly(destination="South Africa"))
    print(airplane_1.location_on_date(date=datetime.datetime(2025, 11, 12)))
    print(airplane_1.location_on_date(date=datetime.datetime(2025, 11, 18)))
    print(airplane_1.avaliable_on_date(date=datetime.datetime(2026, 1, 17), location="The Bahamas"))

    JFK = Airport(city="New York", planes=[airplane_1, airplane_2], scheduled_departures={flight_1.date: flight_1.destination, flight_2.date: flight_2.destination, flight_3.date: flight_3.destination}, scheduled_arrivals={flight_4.date: flight_4.destination, flight_5.date: flight_5.destination, flight_6.date: flight_6.destination})
    print(JFK.info(start_date=datetime.datetime(2025, 1, 1), end_date=datetime.datetime(2026, 11, 10)))
    print(JFK.schedule_flight(destination="Mexico", datetime=datetime.datetime(2027, 1, 1)))