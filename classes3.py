class Flight:

    counter = 1

    def __init__(self, origin, destination, duration):

        # Keep ID number handy
        self.id = Flight.counter
        Flight.counter +=1

        # Keeps track of passengers
        self.passengers = []

        # Flight details
        self.origin = origin

        # Details about the Flight
        self.origin = origin
        self.destionation = destination
        self.duration = duration

        def print_info(self):
                print(f"Flight origin: {self.origin}")
                print(f"Flight destination {self.destination}")
                print(f"Flight duration: {self.duration}")

                print()
                print("Passengers;")
                for passenger in self.passengers:
                    print(f"{passenger.name}")

def delay(self, amount):
    self.duration += amount

def add_passenger(self, p):
    self.passengers.append(p)
        p.flight_id = self.id

class Passenger:

    def __init__(self, name):
        self.name = name

        
def main():

            # flights
            f1 = Flight(origin="Earth", destination="Jupiter", duration="88133")

            # passengers
            ashton = Passenger(name="Ashton")
            alex = Passenger(name="Alex")
            nate = Passenger(name="Nate")

            # add passengers
            f1.add_passenger(Ashton)
            f1.add_passenger(Alex)
            f1.add_passenger(Nate)

            f1.print_info()

if __name__ == "__main__":
    main()