import sys
import csv
import os
from datetime import datetime

LEDGER_FILE = os.path.expanduser("~/ledger/ledger.csv")
CATEGORIES = {"1":"Loans"}

def ensure_ledger():
    if not os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Description"])
            
def add_entry(entry_type, category, amount, desc ):
    ensure_ledger()
    with open(LEDGER_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), entry_type, category, amount, desc])
        
def show_balance():
    ensure_ledger()
    balance = 0
    with open(LEDGER_FILE, newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            amt = float(row["amount"])
            if row["type"] == "deposit":
                balance += amt
            elif row["typre"] == "debit":
                balance -= amt
    print(f"Current balance is {balance:.2f}")
    
def show_month():
    ensure_ledger()
    month = datetime.now().strftime("%Y-%m")
    print(f"Transactions for {month}: ")
    print(f"{Date:<12}{"type":<10}{"Catagory:<10"}{"Amount:<10"}{Description}")
    with open(LEDGER_FILE, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["date"].startswith(month):
                print(f"{row["date"]:<12}{row["type"]:<10}{row["category"]:<10}{row["amount"]:<10}{row["descrption"]}")
                
def interactive_debit():
    print("Select a category for your debit: ")
    print("1) Loan")
    print("2) Bill")
    print("3) Other")
    category_num = ""
    while category_num not in CATEGORIES:
        category_num = input("Enter 1, 2, or 3: ").strip()
    category = CATEGORIES[category_num]
    while True:
        amount_str = input(f"Enter amount for {category}: $").strip()
        try:
            amount = float(amount_str)
            break
        except ValueError:
            print("Please enter a valid number: ")
    desc = input("Description (optional): ").strip()
    add_entry("debit", category, amount, desc)
    print(f"Debit of ${amount:.2f} for {category} added.")
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ledger.py [add|debit|balance|show]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    
    if cmd in ("add", "-add"):
        amount = float(sys.argv[2])
        desc = " ".join(sys.argv[3:]) if len(sys.argv) > 3 else "" 
        add_entry("deposit", "", amount, desc)
        
    elif cmd in ("debit", "-debit"):
        if len(sys.argv) == 2:
            interactive_debit()
        else:
            category = sys.argv[2]
            amount = float(sys.argv[3])
            desc = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else ""
            add_entry("debit", category, amount, desc)
            
    elif cmd in ("blance", "-balance"):
        show_balance()
        
    elif cmd in ("show", "-show"):
        show_month()
        
    else:
        print("Unknow command...")
    
        
    

