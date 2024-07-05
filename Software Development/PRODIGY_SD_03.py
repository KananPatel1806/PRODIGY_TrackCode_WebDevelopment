import json

# Global variable to store contacts
contacts = {}

# File to store contacts data
contacts_file = "contacts.json"


def save_contacts_to_file():
    with open(contacts_file, 'w') as file:
        json.dump(contacts, file)

def load_contacts_from_file():
    global contacts
    try:
        with open(contacts_file, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}

def add_contact(name, phone, email):
    contacts[name] = {'phone': phone, 'email': email}
    save_contacts_to_file()
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if contacts:
        print("Your Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")

def edit_contact(name):
    if name in contacts:
        print(f"Editing contact '{name}':")
        new_phone = input("Enter new phone number (leave blank to keep current): ").strip()
        new_email = input("Enter new email address (leave blank to keep current): ").strip()
        
        if new_phone:
            contacts[name]['phone'] = new_phone
        if new_email:
            contacts[name]['email'] = new_email
        
        save_contacts_to_file()
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts_to_file()
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    load_contacts_from_file()
    
    while True:
        print("\nContact Management System")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Edit a contact")
        print("4. Delete a contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            name = input("Enter name: ").strip()
            phone = input("Enter phone number: ").strip()
            email = input("Enter email address: ").strip()
            add_contact(name, phone, email)
        
        elif choice == '2':
            view_contacts()
        
        elif choice == '3':
            name = input("Enter name of contact to edit: ").strip()
            edit_contact(name)
        
        elif choice == '4':
            name = input("Enter name of contact to delete: ").strip()
            delete_contact(name)
        
        elif choice == '5':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
