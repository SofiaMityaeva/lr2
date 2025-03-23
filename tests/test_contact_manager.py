import pytest
from contacts.contact_manager import Contact, ContactManager

@pytest.fixture
def manager():
    return ContactManager()

@pytest.fixture
def sample_contact():
    return Contact("John Doe", "555-1234", "john@example.com")

def test_add_contact(manager, sample_contact):
    manager.add_contact(sample_contact)
    assert len(manager.list_all_contacts()) == 1
    assert sample_contact in manager.list_all_contacts()

def test_add_duplicate_contact(manager, sample_contact):
    manager.add_contact(sample_contact)
    with pytest.raises(ValueError):
        manager.add_contact(sample_contact)
    assert len(manager.list_all_contacts()) == 1

def test_remove_existing_contact(manager, sample_contact):
    manager.add_contact(sample_contact)
    assert manager.remove_contact(sample_contact.email) is True
    assert len(manager.list_all_contacts()) == 0

def test_remove_non_existent_contact(manager):
    assert manager.remove_contact("nonexistent@example.com") is False

def test_find_by_name(manager):
    contact1 = Contact("Alice", "111-1111", "alice@example.com")
    contact2 = Contact("Alice", "222-2222", "alice2@example.com")
    manager.add_contact(contact1)
    manager.add_contact(contact2)
    
    results = manager.find_by_name("Alice")
    assert len(results) == 2
    assert contact1 in results
    assert contact2 in results

def test_list_all_contacts(manager):
    assert manager.list_all_contacts() == []
    
    contact = Contact("Bob", "333-3333", "bob@example.com")
    manager.add_contact(contact)
    assert len(manager.list_all_contacts()) == 1
    assert contact in manager.list_all_contacts()
