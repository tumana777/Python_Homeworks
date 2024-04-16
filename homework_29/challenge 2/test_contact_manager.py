import unittest
from contact_manager import ContactManager

class TestContactManager(unittest.TestCase):
    def setUp(self):
        self.contacts_book = ContactManager()
        self.contacts_book.add_contact("Alex", 528976)
        self.contacts_book.add_contact("Levan", 453679)
        
    def test_add_contact(self):
        self.assertEqual(self.contacts_book.add_contact("Alex", 589467), "Contact 'Alex' already exists.")
        self.assertEqual(self.contacts_book.add_contact("Oto", 123456), "Contact 'Oto' added successfully.")
        self.assertEqual(self.contacts_book.add_contact("oto", 654789), "Contact 'oto' added successfully.")
        self.assertEqual(self.contacts_book.add_contact("oto", 951357), "Contact 'oto' already exists.")
        self.assertEqual(self.contacts_book.contacts, {'Alex': 528976,"Levan" : 453679, "Oto" : 123456, "oto" : 654789})

    def test_remove_contact(self):
        self.assertEqual(self.contacts_book.remove_contact("Alex"), "Contact 'Alex' removed successfully.")
        self.assertEqual(self.contacts_book.remove_contact("levan"), "Contact 'levan' not found.")
        self.assertEqual(self.contacts_book.remove_contact("Oto"), "Contact 'Oto' not found.")
        self.assertEqual(self.contacts_book.contacts, {"Levan" : 453679})

    def test_search_contact(self):
        self.assertEqual(self.contacts_book.search_contact("Alex"), "Name: Alex, Phone Number: 528976")
        self.assertEqual(self.contacts_book.search_contact("Levan"), "Name: Levan, Phone Number: 453679")
        self.assertEqual(self.contacts_book.search_contact("alex"), "Contact 'alex' not found.")
        self.assertEqual(self.contacts_book.search_contact("Oto"), "Contact 'Oto' not found.")

    def test_display_contacts(self):
        self.assertEqual(self.contacts_book.display_contacts(), "Contacts:\nName: Alex, Phone Number: 528976")
        self.contacts_book.remove_contact("Alex")
        self.contacts_book.remove_contact("Levan")
        self.assertEqual(self.contacts_book.display_contacts(), "No contacts found.")

if __name__ == "__main__":
    unittest.main()