# Air New Zealand Flight Management System

# Parent Class: Flight

class Flight:

    AIRPORT_FEE = 15.00

    def __init__(self, flight_number, departure_city,
                 arrival_city, departure_time,
                 ticket_price):

        self.flight_number = flight_number
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.departure_time = departure_time
        self.ticket_price = ticket_price

    def display_flight(self):
        print(f"Flight Number: {self.flight_number}")
        print(f"Departure City: {self.departure_city}")
        print(f"Arrival City: {self.arrival_city}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Ticket Price: ${self.ticket_price:.2f}")

    def get_route(self):
        return f"{self.departure_city} → {self.arrival_city}"

    def display_price(self):
        print(f"Ticket Price: ${self.ticket_price:.2f}")

    def calculate_total_cost(self):
        return self.ticket_price + Flight.AIRPORT_FEE


# Child Class: PassengerFlight

class PassengerFlight(Flight):

    def __init__(self, flight_number, departure_city,
                 arrival_city, departure_time,
                 ticket_price, passenger_count):

        super().__init__(
            flight_number,
            departure_city,
            arrival_city,
            departure_time,
            ticket_price
        )

        self.passenger_count = passenger_count

    def display_passengers(self):
        print(f"Passengers: {self.passenger_count}")

# Adding methods to manage passengers
    def add_passenger(self):
        self.passenger_count += 1
        print(f"Passenger added. Total passengers: {self.passenger_count}")

    def remove_passenger(self):
        if self.passenger_count > 0:
            self.passenger_count -= 1
            print(f"Passenger removed. Total passengers: {self.passenger_count}")
        else:
            print("No passengers to remove.")


# adding a child class 2 - CargoFlight

class CargoFlight(Flight):

    def __init__(self, flight_number, departure_city,
                 arrival_city, departure_time,
                 ticket_price, cargo_weight):

        super().__init__(
            flight_number,
            departure_city,
            arrival_city,
            departure_time,
            ticket_price
        )

        self.cargo_weight = cargo_weight

    def display_cargo(self):
        print(f"Cargo Weight: {self.cargo_weight} kg")

    def calculate_total_cost(self):
        # Assuming cargo flights have a different fee structure
        cargo_fee = 0.50 * self.cargo_weight  # $0.50 per kg
        return self.ticket_price + Flight.AIRPORT_FEE + cargo_fee

    def flight_type(self):
        return "Cargo Flight"

# Child Class: DomesticFlight

class DomesticFlight(PassengerFlight):

    def __init__(self, flight_number, departure_city,
                 arrival_city, departure_time,
                 ticket_price, passenger_count,
                 baggage_allowance):

        super().__init__(
            flight_number,
            departure_city,
            arrival_city,
            departure_time,
            ticket_price,
            passenger_count
        )

        self.baggage_allowance = baggage_allowance

    def display_baggage(self):
        print(f"Baggage Allowance: {self.baggage_allowance} kg")

    def calculate_total_cost(self):
        return super().calculate_total_cost()

    def flight_type(self):
        return "Domestic Flight"


# InternationalFlight class can be added similarly if needed, with its own specific attributes and methods.

class InternationalFlight(PassengerFlight):

    def __init__(self, flight_number, departure_city,
                 arrival_city, departure_time,
                 ticket_price, passenger_count,
                 visa_required):

        super().__init__(
            flight_number,
            departure_city,
            arrival_city,
            departure_time,
            ticket_price,
            passenger_count
        )

        self.visa_required = visa_required

    def display_visa_info(self):
        if self.visa_required:
            print("Visa Required: Yes")
        else:
            print("Visa Required: No")

    def calculate_total_cost(self):
        # Assuming international flights have an additional fee
        international_fee = 50.00
        return super().calculate_total_cost() + international_fee

    def flight_type(self):
        return "International Flight"

# Main Program

flight1 = DomesticFlight(
    "NZ101",
    "Auckland",
    "Wellington",
    "10:30 AM",
    149.99,
    120,   # passengers
    23     # baggage allowance
)

print("===== AIR NEW ZEALAND DOMESTIC FLIGHT =====")

flight1.display_flight()
print("Route:", flight1.get_route())

flight1.display_passengers()
flight1.display_baggage()

flight1.add_passenger()

print(f"Total Cost (including airport fee): "
      f"${flight1.calculate_total_cost():.2f}")

print("Flight Type:", flight1.flight_type())

# Adding in an international flight example

flight2 = InternationalFlight(
    "NZ202",
    "Auckland",
    "Sydney",
    "2:00 PM",
    299.99,
    150,   # passengers
    True   # visa required
)

print("\n===== AIR NEW ZEALAND INTERNATIONAL FLIGHT =====")

flight2.display_flight()
flight2.display_price()

print("Route:", flight2.get_route())
flight2.display_passengers()

flight2.display_visa_info()

print(f"Total Cost (including airport fee and international fee): "
      f"${flight2.calculate_total_cost():.2f}")

# adding in the cargo flight example

print("\n===== AIR NEW ZEALAND CARGO FLIGHT =====")

cargo1 = CargoFlight(
    "NZ303",
    "Auckland",
    "Los Angeles",
    "5:00 PM",
    499.99,
    2000  # cargo weight in kg
)

cargo1.display_flight()
cargo1.display_cargo()

print(f"Total Cost (including airport fee and cargo fee): "
      f"${cargo1.calculate_total_cost():.2f}")