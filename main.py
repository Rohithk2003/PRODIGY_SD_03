import json, os


# contact management system
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    if not os.path.exists("contacts.json"):
        with open("contacts.json", "w") as file:
            json.dump([], file)
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
    contacts.append(contact)
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)
    print("Contact added successfully.")


def view_contacts():
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
    for contact in contacts:
        print(
            f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
        )


def edit_contact():
    name = input("Enter name: ")
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
    for contact in contacts:
        if contact["name"] == name:
            print(
                f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
            )
            contacts.remove(contact)
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            contact = {"name": name, "phone": phone, "email": email}
            contacts.append(contact)
            with open("contacts.json", "w") as file:
                json.dump(contacts, file)
            print("Contact updated successfully.")
            break
    else:
        print("Contact not found.")


def search_contact():
    name = input("Enter name: ")
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
    for contact in contacts:
        if contact["name"] == name:
            print(
                f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}"
            )
            break
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name: ")
    with open("contacts.json", "r") as file:
        contacts = json.load(file)
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            with open("contacts.json", "w") as file:
                json.dump(contacts, file)
            print("Contact deleted successfully.")
            break
    else:
        print("Contact not found.")


if __name__ == "__main__":
    while True:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Search Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            edit_contact()
        elif choice == 4:
            search_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            break
        else:
            print("Invalid choice. Try again.")
