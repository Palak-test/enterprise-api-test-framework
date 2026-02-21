import unittest
from src.email_utility import EmailUtility

class TestEmailUtility(unittest.TestCase):
    def test_send_email_invalid_server(self):
        result = EmailUtility.send_email(
            smtp_server="invalid.server",
            port=587,
            sender_email="test@example.com",
            receiver_email="test@example.com",
            subject="Test",
            body="This is a test email."
        )
        self.assertIsInstance(result, str)
        self.assertTrue("failed" in result or "Errno" in result or "error" in result)

if __name__ == '__main__':
    unittest.main()
