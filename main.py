#!/usr/bin/env python3

import os
import chankfinance as cf

db_file = "finance.db"
folder= "data"

#database init and check to see if file exists
def check_db(folder_path, db_file):
    if os.path.isfile(os.path.join(folder_path, db_file)):
        print(f"Database file '{db_file}' found in folder '{folder_path}'")
        return cf.load_db(f"{folder}/{db_file}")
    else:
        print(f"Database file '{db_file}' not found in folder '{folder_path}'\n[init] initializing database")
        return cf.initialize_db(f"{folder}/{db_file}")

def parse_deposit(input_str):
    # Split the input string by space
    parts = input_str.split()

    # Check if the input string is in the correct format
    if len(parts) != 2:
        print("Invalid input format. Please enter in the format: deposit {amount}")
        return None

    # Try to convert the second part (amount) to an integer
    try:
        amount = float(parts[1])
        return amount
    except ValueError:
        print("Invalid amount. Please enter a valid float amount.")
        return None       

if __name__ == "__main__":

    #Create a connection to the database

    print("\n\nWelcome to chanks finance script")

    end = False
    
    while not end:
        #prompt the user to enter something
        #commands end/exit, deposit {amount}
        prompt = input(">")
        if prompt[0:7] == "deposit":
            amnt = parse_deposit(prompt)
            print(cf.input_deposit(amnt))
        elif prompt == "exit" or prompt == "end":
            end = True
            print("\n\nlater yall")
        elif prompt[0:4] == 'list':
            print(cf.list_table())
        elif prompt[0:5] == 'reset':
            ans = input("\nare you sure?(y/n)\n>")
            if ans == "y":
                cf.reset()
                print("[success] db was reset")
            else:
                print("[error] db not reset")







