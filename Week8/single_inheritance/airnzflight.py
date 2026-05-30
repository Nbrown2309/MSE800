# Air New Zealand Flight Management System

# Parent Class: Flight

class Flight:

    def __init__(self, flight_number, departure_city,
                 arrival_city, departure_time,
                 ticket_price):

        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        
        #Adding in Cost of flights (including aiport fee) 
        self.ticket_price = ticket_price

    def display_flight(self):
        print(f"Flight Number: {self.flight_number}")
        print(f"Departure City: {self.departure_city}")
        print(f"Arrival City: {self.arrival_city}")
        print(f"Departure Time: {self.departure_time}")

    def get_route(self):
        return f"{self.departure_city} → {self.arrival_city}"

    def display_price(self):
        print(f"Ticket Price: ${self.ticket_price:.2f}")


# Child Class: DomesticFlight

class DomesticFlight(Flight):

    def __init__(self, flight_number, departure_city,
                 arrival_city, departure_time,
                 ticket_price,
                 baggage_allowance):

        # Inherit attributes from Flight
        super().__init__(
            flight_number,
            departure_city,
            arrival_city,
            departure_time,
            ticket_price
        )

        # DomesticFlight specific attribute
        self.baggage_allowance = baggage_allowance

    def display_baggage(self):
        print(f"Baggage Allowance: {self.baggage_allowance} kg")

    # Additional DomesticFlight method
    def calculate_total_cost(self):

        airport_fee = 15.00
        total = self.ticket_price + airport_fee

        return total


# Main Program

flight1 = DomesticFlight(
    "NZ101",
    "Auckland",
    "Wellington",
    "10:30 AM",
    149.99,
    23
)

print("===== AIR NEW ZEALAND DOMESTIC FLIGHT =====")

flight1.display_flight()
flight1.display_price()

print("Route:", flight1.get_route())

flight1.display_baggage()

print(f"Total Cost (including airport fee): "
      f"${flight1.calculate_total_cost():.2f}")