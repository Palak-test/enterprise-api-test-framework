import unittest
from src.random_ticket import random_support_ticket

class TestRandomTicket(unittest.TestCase):
    def test_random_ticket_keys(self):
        ticket = random_support_ticket()
        self.assertIn("ticket_id", ticket)
        self.assertIn("user", ticket)
        self.assertIn("issue", ticket)
        self.assertIn("created_at", ticket)
        self.assertIn("status", ticket)
        self.assertTrue(ticket["status"] in ["open", "closed", "pending", "resolved"])
        self.assertTrue(isinstance(ticket["issue"], str))

if __name__ == "__main__":
    unittest.main()
