
class Passenger():
    def __init__(self, name:str = "Unknown", surname:str = "Unknown"):
        self.name = name
        self.surname = surname
        self.x = 0
        self.y = 0
        self.bus = None

    #======= Getter =======#
    """
    @property
    def name(self):
        return self.name

    @property
    def surname(self):
        return self.surname
    
    @property
    def coordinates(self):
        return (self.x, self.y)
    #========================#
    """

    #======= Passenger Methods =======#
    def set_coordinates(self, x, y):
        if (type(x) in (float)) and (type(y) in (float)):
            self.x = x
            self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def get_on_bus(self, bus):
        bus.add_passenger(self)
        self.bus = bus

    def get_off_bus(self):
        self.bus = None

    def get_bus_name(self):
        if self.bus:
            return self.bus.number
        return "The passenger is not on the bus."

    def __str__(self):
        return f"""
        ===== Passenger Information =====
        Passenger Name: {self.name}
        Passenger Surname: {self.surname}
        Passenger Coordinates: ({self.x},{self.y})
        """
    #==========================#

    """
    @surname.setter
    def surname(self, value):
        self._surname = value

    @name.setter
    def name(self, value):
        self._name = value
    """

class Bus():
    
    def __init__(self, number:str = "Unknown", route:str = "Unknown"):
        self.number = number
        self.passengers = []
        self.x = 0
        self.y = 0
        self.passenger_count = 0
        self.route = route

    #======= Getter =======#
    """
    @property
    def number(self):
        return self.number

    @property
    def coordinates(self):
        return(self.x, self.y)
    #======================#


    #======= Setter =======#
    @number.setter
    def change_number(self, new_number):
        self.number = new_number
    """
    #======================#


    #======= Bus Methods =======#
    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        self.passenger_count += 1

    def remove_passenger(self, passenger):
        for person in self.passengers:
            if ((passenger.name == person.name) and (passenger.surname == person.surname)):
                self.passengers.remove(person)
                self.passenger_count -= 1

    def show_passengers(self):
        i = 1
        for person in self.passengers:
            print(f"Passenger {i}: {person.name} {person.surname}",sep="\n",end="\n")
            i += 1

    def move(self, x, y):
        self.x += x
        self.y += y
        for person in self.passengers:
            person.move(x,y)

    def __str__(self):
        return f"""
        
        ===== Bus Info Table =====
        Bus Number: {self.number}
        Bus Current Passenger Count: {self.passenger_count}
        Bus Route: {self.route}
        Bus Coordinates: ({self.x},{self.y})
        """
        #Bus Current Passengers: {self.passengers}
    #==========================#

def main():
    p1 = Passenger("Azar", "Osmanzada")
    p2 = Passenger("Ruslan", "Alquliyev")
    p3 = Passenger("Hajiahmad", "Ahmadzada")
    p4 = Passenger("Jabrayil", "Abdinbayov")
    p5 = Passenger("Farid", "Huseynli")

    print(p1)

    b1 = Bus("125", "28 May")

    print(b1)

    b1.add_passenger(p1)
    b1.add_passenger(p2)
    b1.add_passenger(p3)
    b1.add_passenger(p4)

    print(b1)
    print(p3)

    b1.move(10,12)
    print(b1)
    print(p4)

    b1.show_passengers()

    b1.remove_passenger(p3)
    b1.show_passengers()
    print(b1)

if __name__ == "__main__":
    main()