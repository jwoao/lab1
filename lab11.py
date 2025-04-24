import psycopg2
import csv

conn = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="skzf0325",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def insert_from_csv():
    try:
        with open('phonebook_data.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cur.execute("""
                    INSERT INTO phonebook (first_name, last_name, phone_number)
                    VALUES (%s, %s, %s)
                    ON CONFLICT (phone_number) DO NOTHING
                """, (row[0], row[1], row[2]))
        conn.commit()
        print("✅ Data uploaded from CSV.")
    except Exception as e:
        conn.rollback()
        print("❌ Error uploading from CSV:", e)

def upsert_user():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    phone = input("Enter phone number: ")
    try:
        cur.execute("CALL upsert_user(%s, %s, %s)", (fname, lname, phone))
        conn.commit()
        print("✅ User inserted or updated.")
    except Exception as e:
        conn.rollback()
        print("❌ Error:", e)

def insert_many_users():
    fnames, lnames, phones = [], [], []
    n = int(input("How many users to insert? "))
    for _ in range(n):
        fnames.append(input("First name: "))
        lnames.append(input("Last name: "))
        phones.append(input("Phone number: "))
    try:
        cur.callproc('insert_many_users', (fnames, lnames, phones))
        invalids = cur.fetchone()[0]
        conn.commit()
        if invalids:
            print("⚠️ Invalid phone numbers:", invalids)
        else:
            print("✅ All users inserted.")
    except Exception as e:
        conn.rollback()
        print("❌ Error inserting users:", e)

def search_by_pattern():
    pattern = input("Enter pattern to search: ")
    try:
        cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("ℹ️ No matches found.")
    except Exception as e:
        print("❌ Error searching:", e)

def get_paginated_contacts():
    limit = int(input("Enter number of results: "))
    offset = int(input("Enter offset: "))
    try:
        cur.execute("SELECT * FROM get_contacts(%s, %s)", (limit, offset))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print("❌ Error fetching paginated results:", e)

def delete_contact():
    value = input("Enter name or phone to delete: ")
    try:
        cur.execute("CALL delete_by_name_or_phone(%s)", (value,))
        conn.commit()
        print("✅ Contact(s) deleted.")
    except Exception as e:
        conn.rollback()
        print("❌ Error deleting contact:", e)

def show_all():
    try:
        cur.execute("SELECT * FROM phonebook ORDER BY id")
        rows = cur.fetchall()
        print("\n📖 PhoneBook:")
        for row in rows:
            print(row)
        print("")
    except Exception as e:
        print("❌ Error showing contacts:", e)

def menu():
    while True:
        print("\n📱 PhoneBook Menu")
        print("1. Upload from CSV")
        print("2. Add or update user (upsert)")
        print("3. Insert multiple users")
        print("4. Search by pattern")
        print("5. Paginated view")
        print("6. Delete by name or phone")
        print("7. Show all contacts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            upsert_user()
        elif choice == '3':
            insert_many_users()
        elif choice == '4':
            search_by_pattern()
        elif choice == '5':
            get_paginated_contacts()
        elif choice == '6':
            delete_contact()
        elif choice == '7':
            show_all()
        elif choice == '0':
            break
        else:
            print("❌ Invalid choice. Try aga1in.")

    cur.close()
    conn.close()
    print("👋 Goodbye!")

menu()