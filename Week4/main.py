from database import *


# SETUP DATABASE


def setup_database():

    create_customers_table()
    create_employees_table()
    create_currencies_table()
    create_exchange_rates_table()
    create_transactions_table()
    create_payments_table()


# Adding Customer 

def add_customer():

    conn = create_connection()
    cursor = conn.cursor()

    print("\n=== ADD CUSTOMER ===")

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    phone = input("Phone Number: ")
    address = input("Address: ")

    cursor.execute("""
        INSERT INTO Customers
        (FirstName, LastName, Email, PhoneNumber, Address)

        VALUES (?, ?, ?, ?, ?)
    """, (first_name, last_name, email, phone, address))

    conn.commit()
    conn.close()

    print("Customer added successfully!")


# View Customers

def view_customers():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Customers")

    customers = cursor.fetchall()

    print("\n=== CUSTOMERS ===")

    for customer in customers:
        print(customer)

    conn.close()


# Update Customer

def update_customer():

    conn = create_connection()
    cursor = conn.cursor()

    customer_id = input("Enter Customer ID: ")

    new_phone = input("New Phone Number: ")
    new_address = input("New Address: ")

    cursor.execute("""
        UPDATE Customers

        SET PhoneNumber = ?,
            Address = ?

        WHERE CustomerID = ?
    """, (new_phone, new_address, customer_id))

    conn.commit()
    conn.close()

    print("Customer updated successfully!")


# Delete the customers information

def delete_customer():

    conn = create_connection()
    cursor = conn.cursor()

    customer_id = input("Enter Customer ID to delete: ")

    cursor.execute("""
        DELETE FROM Customers
        WHERE CustomerID = ?
    """, (customer_id,))

    conn.commit()
    conn.close()

    print("Customer deleted successfully!")


# Add Currency 

def add_currency():

    conn = create_connection()
    cursor = conn.cursor()

    print("\n=== ADD CURRENCY ===")

    currency_name = input("Currency Name: ")
    currency_code = input("Currency Code: ")
    country = input("Country: ")
    symbol = input("Symbol: ")
    status = input("Status: ")

    cursor.execute("""
        INSERT INTO Currencies

        (CurrencyName, CurrencyCode,
         Country, Symbol, Status)

        VALUES (?, ?, ?, ?, ?)
    """, (
        currency_name,
        currency_code,
        country,
        symbol,
        status
    ))

    conn.commit()
    conn.close()

    print("Currency added successfully!")


# View Currencies 

def view_currencies():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Currencies")

    currencies = cursor.fetchall()

    print("\n=== CURRENCIES ===")

    for currency in currencies:
        print(currency)

    conn.close()


# Add Transaction 

def add_transaction():

    conn = create_connection()
    cursor = conn.cursor()

    print("\n=== ADD TRANSACTION ===")

    customer_id = input("Customer ID: ")
    employee_id = input("Employee ID: ")

    from_currency = input("From Currency ID: ")
    to_currency = input("To Currency ID: ")

    amount_sent = float(input("Amount Sent: "))
    amount_received = float(input("Amount Received: "))

    transaction_date = input("Date (YYYY-MM-DD): ")

    cursor.execute("""
        INSERT INTO Transactions

        (CustomerID, EmployeeID,
         FromCurrencyID, ToCurrencyID,
         AmountSent, AmountReceived,
         TransactionDate)

        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        customer_id,
        employee_id,
        from_currency,
        to_currency,
        amount_sent,
        amount_received,
        transaction_date
    ))

    conn.commit()
    conn.close()

    print("Transaction added successfully!")


# Viewing the following Transactions 

def view_transactions():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Transactions")

    transactions = cursor.fetchall()

    print("\n=== TRANSACTIONS ===")

    for transaction in transactions:
        print(transaction)

    conn.close()


# Add Payment for the customers

def add_payment():

    conn = create_connection()
    cursor = conn.cursor()

    print("\n=== ADD PAYMENT ===")

    transaction_id = input("Transaction ID: ")

    payment_method = input("Payment Method: ")
    payment_status = input("Payment Status: ")

    payment_date = input("Payment Date: ")

    total_amount = float(input("Total Amount: "))

    cursor.execute("""
        INSERT INTO Payments

        (TransactionID, PaymentMethod,
         PaymentStatus, PaymentDate,
         TotalAmount)

        VALUES (?, ?, ?, ?, ?)
    """, (
        transaction_id,
        payment_method,
        payment_status,
        payment_date,
        total_amount
    ))

    conn.commit()
    conn.close()

    print("Payment added successfully!")


# View Payments

def view_payments():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Payments")

    payments = cursor.fetchall()

    print("\n=== PAYMENTS ===")

    for payment in payments:
        print(payment)

    conn.close()


# Following Menu System

def menu():

    while True:

        print("\n================================")
        print(" MONEY EXCHANGE DATABASE SYSTEM ")
        print("================================")

        print("1. Add Customer")
        print("2. View Customers")
        print("3. Update Customer")
        print("4. Delete Customer")

        print("5. Add Currency")
        print("6. View Currencies")

        print("7. Add Transaction")
        print("8. View Transactions")

        print("9. Add Payment")
        print("10. View Payments")

        print("11. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            update_customer()

        elif choice == "4":
            delete_customer()

        elif choice == "5":
            add_currency()

        elif choice == "6":
            view_currencies()

        elif choice == "7":
            add_transaction()

        elif choice == "8":
            view_transactions()

        elif choice == "9":
            add_payment()

        elif choice == "10":
            view_payments()

        elif choice == "11":
            print("Exiting system...")
            break

        else:
            print("Invalid choice.")


# ==========================================
# MAIN PROGRAM
# ==========================================

def main():

    setup_database()
    menu()


if __name__ == "__main__":
    main()