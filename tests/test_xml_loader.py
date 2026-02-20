import unittest
from src.xml_loader import load_xml_data

class TestXMLLoader(unittest.TestCase):
    def test_load_xml_data(self):
        root = load_xml_data("tests/test_data.xml")
        users = root.findall("user")
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].find("username").text, "user1")
        self.assertEqual(users[1].find("email").text, "user2@example.com")

if __name__ == "__main__":
    unittest.main()
