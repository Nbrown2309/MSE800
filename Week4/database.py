import sqlite3


# ==========================================
# CREATE DATABASE CONNECTION
# ==========================================

def create_connection():

    conn = sqlite3.connect("money_exchange.db")
    return conn


# ==========================================
# CREATE CUSTOMERS TABLE
# ==========================================

def create_customers_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Customers (

            CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,

            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,

            Email TEXT UNIQUE,
            PhoneNumber TEXT,
            Address TEXT
        )
    """)

    conn.commit()
    conn.close()


# ==========================================
# CREATE EMPLOYEES TABLE
# ==========================================

def create_employees_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employees (

            EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,

            FirstName TEXT NOT NULL,
            LastName TEXT NOT NULL,

            Role TEXT,
            Email TEXT,
            PhoneNumber TEXT
        )
    """)

    conn.commit()
    conn.close()


# ==========================================
# CREATE CURRENCIES TABLE
# ==========================================

def create_currencies_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Currencies (

            CurrencyID INTEGER PRIMARY KEY AUTOINCREMENT,

            CurrencyName TEXT NOT NULL,
            CurrencyCode TEXT NOT NULL,

            Country TEXT,
            Symbol TEXT,
            Status TEXT
        )
    """)

    conn.commit()
    conn.close()


# ==========================================
# CREATE EXCHANGE RATES TABLE
# ==========================================

def create_exchange_rates_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ExchangeRates (

            RateID INTEGER PRIMARY KEY AUTOINCREMENT,

            FromCurrencyID INTEGER,
            ToCurrencyID INTEGER,

            ExchangeRate REAL,
            LastUpdated TEXT,
            RateStatus TEXT,

            FOREIGN KEY (FromCurrencyID)
                REFERENCES Currencies(CurrencyID),

            FOREIGN KEY (ToCurrencyID)
                REFERENCES Currencies(CurrencyID)
        )
    """)

    conn.commit()
    conn.close()


# ==========================================
# CREATE TRANSACTIONS TABLE
# ==========================================

def create_transactions_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Transactions (

            TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,

            CustomerID INTEGER,
            EmployeeID INTEGER,

            FromCurrencyID INTEGER,
            ToCurrencyID INTEGER,

            AmountSent REAL,
            AmountReceived REAL,

            TransactionDate TEXT,

            FOREIGN KEY (CustomerID)
                REFERENCES Customers(CustomerID),

            FOREIGN KEY (EmployeeID)
                REFERENCES Employees(EmployeeID),

            FOREIGN KEY (FromCurrencyID)
                REFERENCES Currencies(CurrencyID),

            FOREIGN KEY (ToCurrencyID)
                REFERENCES Currencies(CurrencyID)
        )
    """)

    conn.commit()
    conn.close()


# ==========================================
# CREATE PAYMENTS TABLE
# ==========================================

def create_payments_table():

    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Payments (

            PaymentID INTEGER PRIMARY KEY AUTOINCREMENT,

            TransactionID INTEGER,

            PaymentMethod TEXT,
            PaymentStatus TEXT,

            PaymentDate TEXT,
            TotalAmount REAL,

            FOREIGN KEY (TransactionID)
                REFERENCES Transactions(TransactionID)
        )
    """)

    conn.commit()
    conn.close()