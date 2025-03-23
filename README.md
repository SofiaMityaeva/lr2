# Contact Management Application

A simple Python-based contact management system that allows you to store, manage, and search contacts. The application is built with clean code practices and includes a comprehensive test suite using `pytest`.

---

## Features

- **Add Contacts**: Store contacts with name, phone number, and email.
- **Remove Contacts**: Delete contacts by email.
- **Search Contacts**: Find contacts by name (case-insensitive and partial match supported).
- **List All Contacts**: View all stored contacts.
- **Input Validation**: Ensures valid email format and prevents empty fields.
- **Duplicate Prevention**: Prevents adding contacts with duplicate emails.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/contact-app.git
   cd contact-app
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

```bash
pip install pytest
```

## Usage

### Running the Application

You can use the `ContactManager` class in your Python code:

```python
from contacts.contact_manager import Contact, ContactManager

# Create a manager instance
manager = ContactManager()

# Add a contact
contact = Contact("John Doe", "555-1234", "john@example.com")
manager.add_contact(contact)

# Find contacts by name
results = manager.find_by_name("John")

# Remove a contact
manager.remove_contact("john@example.com")

# List all contacts
all_contacts = manager.list_all_contacts()
```

### Testing

The application includes a comprehensive test suite using pytest. To run the tests:

1. Navigate to the project root directory.
2. Run the tests:
   ```bash
   PYTHONPATH=. pytest tests/ -v
   ```
