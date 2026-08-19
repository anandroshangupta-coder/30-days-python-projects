# ==========================================
# Day 12 - Contact Book
# 30 Days Python GitHub Project Challenge
# ==========================================

print("======================================")
print("             CONTACT BOOK")
print("======================================")

# Store contacts
contacts = {}


# Add contact
def add_contact():
    name = input("\nEnter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("✅ Contact added successfully!")


# View contacts
def view_contacts():
    print("\n======================================")
    print("            ALL CONTACTS")
    print("======================================")

    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"\nName  : {name}")
            print(f"Phone : {details['phone']}")
            print(f"Email : {details['email']}")

    print("======================================")


# Search contact
def search_contact():
    name = input("\nEnter contact name to search: ")

    if name in contacts:
        print("\n======================================")
        print("          CONTACT FOUND")
        print("======================================")
        print(f"Name  : {name}")
        print(f"Phone : {contacts[name]['phone']}")
        print(f"Email : {contacts[name]['email']}")
        print("======================================")
    else:
        print("❌ Contact not found.")


# Update contact
def update_contact():
    name = input("\nEnter contact name to update: ")

    if name in contacts:

        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")

        contacts[name]["phone"] = phone
        contacts[name]["email"] = email

        print("✅ Contact updated successfully!")

    else:
        print("❌ Contact not found.")


# Delete contact
def delete_contact():
    name = input("\nEnter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("✅ Contact deleted successfully!")
    else:
        print("❌ Contact not found.")


# Main menu
while True:

    print("\nChoose an option:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\n======================================")
        print("       Thank You! Goodbye 👋")
        print("======================================")
        break

    else:
        print("❌ Invalid choice! Please select 1-6.")