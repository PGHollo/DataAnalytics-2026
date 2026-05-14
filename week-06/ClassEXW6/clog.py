import os

FILENAME = "interactions.txt"


def create_log():
  
    with open(FILENAME, "w") as file:
        file.write("=== Customer Interaction Log ===\n")
        file.write("Date | Customer | Issue | Rep\n")
    print("Log file created.")


def add_records():
   
    records = [
        "2025-05-01 | Alice Nguyen | Billing query | J. Park\n",
        "2025-05-01 | Bob Carter | Login issue | S. Diaz\n",
        "2025-05-02 | Carol Singh | Refund request | J. Park\n",
        "2025-05-02 | Alice Nguyen | Follow-up | M. Lee\n"]

    with open(FILENAME, "a") as file:
        file.writelines(records)

    print("Records added.")


def show_log():
   
    try:
        with open(FILENAME, "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Log file not found. Create it first.")


def search_customer(name):
   
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        for line in lines:
            if name.lower() in line.lower():
                print(line.strip())

    except FileNotFoundError:
        print("Log file not found. Create it first.")


def count_entries():
 
    try:
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        count = len(lines) - 2
        print(f"Total entries: {count}")

    except FileNotFoundError:
        print("Log file not found. Create it first.")


def update_header():
  
    try:
        with open(FILENAME, "r+") as file:
            lines = file.readlines()
            count = len(lines) - 2

            lines[0] = f"=== Customer Interaction Log | Entries: {count} ===\n"

            file.seek(0)
            file.writelines(lines)
            file.truncate()

        print("Header updated.")

    except FileNotFoundError:
        print("Log file not found. Create it first.")


# Main program
if not os.path.exists(FILENAME):
    create_log()

add_records()
show_log()
search_customer("Alice Nguyen")
count_entries()
update_header()