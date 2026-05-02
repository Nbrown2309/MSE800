
from database import (
    create_customers_table,
    create_employees_table,
    create_currencies_table,
    create_exchange_rates_table,
    create_transactions_table,
    create_payments_table,
    create_connection
)


# CREATE ALL TABLES

def setup_database():
    create_customers_table()
    create_employees_table()
    create_currencies_table()
    create_exchange_rates_table()
    create_transactions_table()
    create_payments_table()


# ADD CUSTOMER

def add_customer():

    conn = create_connection()
    cursor = conn.cursor()

    print("\n=== ADD CUSTOMER ===")

    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    address = input("Enter address: ")

    cursor.execute("""
        INSERT INTO Customers
        (FirstName, LastName, Email, PhoneNumber, Address)
        VALUES (?, ?, ?, ?, ?)
    """, (first_name, last_name, email, phone, address))

    conn.commit()
    conn.close()

    print("Customer added successfully!")


# VIEW CUSTOMERS

def view_customers():

    conn = create_connection()
    cursor = conn.cursor()

    print("\n=== CUSTOMER LIST ===")

    cursor.execute("SELECT * FROM Customers")

    customers = cursor.fetchall()

    if len(customers) == 0:
        print("No customers found.")

    else:
        for customer in customers:
            print(customer)

    conn.close()

# DELETE CUSTOMER

def delete_customer():

    conn = create_connection()
    cursor = conn.cursor()

    print("\n=== DELETE CUSTOMER ===")

    customer_id = input("Enter Customer ID to delete: ")

    cursor.execute("""
        DELETE FROM Customers
        WHERE CustomerID = ?
    """, (customer_id,))

    conn.commit()
    conn.close()

    print("Customer deleted successfully!")


# MAIN MENU

def menu():

    while True:

        print("\n===================================")
        print(" MONEY EXCHANGE DATABASE SYSTEM ")
        print("===================================")

        print("1. Add Customer")
        print("2. View Customers")
        print("3. Delete Customer")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        # ADD CUSTOMER
        if choice == "1":
            add_customer()

        # VIEW CUSTOMERS
        elif choice == "2":
            view_customers()

        # DELETE CUSTOMER
        elif choice == "3":
            delete_customer()

        # EXIT PROGRAM
        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid option. Try again.")


# RUN PROGRAM

def main():

    setup_database()
    menu()


if __name__ == "__main__":
    main()