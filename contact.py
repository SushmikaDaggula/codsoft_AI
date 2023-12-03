class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"\nContact '{contact.name}' added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts available.")
        else:
            for idx, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {idx}:\n{contact}")

    def search_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if (
                search_term.lower() in contact.name.lower()
                or search_term in contact.phone_number
            ):
                results.append(contact)
        return results

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name.lower() == old_name.lower():
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                print(f"\nContact '{old_name}' updated successfully!")
                return
        print(f"\nContact '{old_name}' not found.")

    def delete_contact(self, contact_name):
        for contact in self.contacts:
            if contact.name.lower() == contact_name.lower():
                self.contacts.remove(contact)
                print(f"\nContact '{contact_name}' deleted successfully!")
                return
        print(f"\nContact '{contact_name}' not found.")

    def user_interface(self):
        print("Welcome to the Contact Management System!")

        while True:
            print("\n1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Update Contact")
            print("5. Delete Contact")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")

            if choice == '1':
                name = input("Enter contact name: ")
                phone_number = input("Enter phone number: ")
                email = input("Enter email address: ")
                address = input("Enter address: ")
                new_contact = Contact(name, phone_number, email, address)
                self.add_contact(new_contact)

            elif choice == '2':
                self.view_contacts()

            elif choice == '3':
                search_term = input("Enter contact name or phone number to search: ")
                search_results = self.search_contact(search_term)
                if search_results:
                    print("\nSearch Results:")
                    for idx, result in enumerate(search_results, start=1):
                        print(f"\nResult {idx}:\n{result}")
                else:
                    print("\nNo matching contacts found.")

            elif choice == '4':
                old_name = input("Enter the name of the contact to update: ")
                new_name = input("Enter new contact name: ")
                new_phone = input("Enter new phone number: ")
                new_email = input("Enter new email address: ")
                new_address = input("Enter new address: ")
                updated_contact = Contact(new_name, new_phone, new_email, new_address)
                self.update_contact(old_name, updated_contact)

            elif choice == '5':
                contact_name = input("Enter the name of the contact to delete: ")
                self.delete_contact(contact_name)

            elif choice == '6':
                print("Thanks for using the Contact Management System!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.user_interface()
