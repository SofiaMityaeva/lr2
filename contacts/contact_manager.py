class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __eq__(self, other):
        return self.email == other.email


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        if any(c.email == contact.email for c in self.contacts):
            raise ValueError("Contact with this email already exists")
        self.contacts.append(contact)
        return True

    def remove_contact(self, email):
        for contact in self.contacts:
            if contact.email == email:
                self.contacts.remove(contact)
                return True
        return False

    def find_by_name(self, name):
        return [contact for contact in self.contacts if contact.name == name]

    def list_all_contacts(self):
        return self.contacts.copy()
