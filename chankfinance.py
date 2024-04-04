import sqlite3
from datetime import datetime
from prettytable import PrettyTable

"""
API
"""

#initialize the database
def initialize_db(db_file):
    # Connect to the SQLite database file
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Create a table named 'finance' with the specified columns
    cursor.execute('''CREATE TABLE IF NOT EXISTS finance (
                        id INTEGER PRIMARY KEY,
                        month TEXT,
                        date TEXT,
                        deposit REAL,
                        expenses REAL,
                        investment REAL,
                        extra REAL
                    )''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def load_db(db_file):
    conn = sqlite3.connect(db_file)
    conn.close()

#DEPOSIT()
def input_deposit(amount):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("data/finance.db")
        cursor = conn.cursor()

        # Get current date and month
        current_date = datetime.now().strftime("%Y-%m-%d")
        current_month = datetime.now().strftime("%Y-%m")

        # Calculate amounts for each column based on percentages
        deposit_amount = amount
        expenses_amount = amount * 0.7
        investment_amount = amount * 0.2
        extra_amount = amount * 0.1

        # Insert data into the database
        cursor.execute('''INSERT INTO finance (month, date, deposit, expenses, investment, extra)
                          VALUES (?, ?, ?, ?, ?, ?)''',
                       (current_month, current_date, deposit_amount, expenses_amount, investment_amount, extra_amount))

        # Commit the transaction and close the connection
        conn.commit()
        msg = f"[success] deposited {amount}"
    except:
        msg = "[error] could not deposit the amount"
    return msg

def list_table():
    # Connect to the SQLite database
    conn = sqlite3.connect("data/finance.db")
    cursor = conn.cursor()

    # Fetch data from the database
    cursor.execute('''SELECT * FROM finance''')
    rows = cursor.fetchall()
    conn.close()

    # Create a pretty table
    table = PrettyTable(["ID", "Month", "Date", "Deposit", "Expenses", "Investment", "Extra"])

    # Add rows to the table
    for row in rows:
        table.add_row(row)

    # Print the table
    return table

def reset():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect("data/finance.db")
        cursor = conn.cursor()

        # Delete all records from the table
        cursor.execute("DELETE FROM finance;")

        # Commit the changes
        conn.commit()

        print("Table 'finance' has been reset successfully.")

    except sqlite3.Error as e:
        print("Error:", e)

    finally:
        # Close the connection
        if conn:
            conn.close()
