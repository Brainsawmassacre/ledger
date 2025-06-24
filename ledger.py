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
            
def add_entry( ):
    ensure_ledger()
    with open(LEDGER_FILE, "a", newline="") as f:
        
        
