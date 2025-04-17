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


cur.execute("DROP TABLE IF EXISTS phonebook")
cur.execute("""
    CREATE TABLE phonebook (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        phone_number VARCHAR(20) UNIQUE NOT NULL
    )
""")
conn.commit()


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

# Insert manually
def insert_manually():
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    phone = input("Enter phone number: ")
    try:
        cur.execute("""
            INSERT INTO phonebook (first_name, last_name, phone_number)
            VALUES (%s, %s, %s)
        """, (fname, lname, phone))
        conn.commit()
        print("✅ Contact added.")
    except Exception as e:
        conn.rollback()
        print("❌ Error adding contact:", e)


def update_contact():
    phone = input("Enter the phone number of the contact to update: ")
    field = input("What do you want to update? (first_name / last_name / phone_number): ")
    new_value = input(f"Enter new value for {field}: ")
    try:
        cur.execute(f"UPDATE phonebook SET {field} = %s WHERE phone_number = %s", (new_value, phone))
        conn.commit()
        print("✅ Contact updated.")
    except Exception as e:
        conn.rollback()
        print("❌ Error updating contact:", e)

def search_contacts():
    search = input("Search by (first_name / last_name / phone_number): ")
    value = input(f"Enter value for {search}: ")
    try:
        cur.execute(f"SELECT * FROM phonebook WHERE {search} = %s", (value,))
        rows = cur.fetchall()
        if rows:
            for row in rows:
                print(row)
        else:
            print("ℹ️ No matching contacts found.")
    except Exception as e:
        conn.rollback()
        print("❌ Error searching:", e)

def delete_contact():
    phone = input("Enter phone number of contact to delete: ")
    try:
        cur.execute("DELETE FROM phonebook WHERE phone_number = %s", (phone,))
        conn.commit()
        print("✅ Contact deleted.")
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
        conn.rollback()
        print("❌ Error showing contacts:", e)

def menu():
    while True:
        print("\n📱 PhoneBook Menu")
        print("1. Upload from CSV")
        print("2. Add contact manually")
        print("3. Update contact")
        print("4. Search contacts")
        print("5. Delete contact")
        print("6. Show all contacts")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            insert_manually()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            search_contacts()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            show_all()
        elif choice == '0':
            break
        else:
            print("❌ Invalid choice. Try again.")

    cur.close()
    conn.close()
    print("👋 Goodbye!")

menu()
