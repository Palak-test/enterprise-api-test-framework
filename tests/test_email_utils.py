import unittest
from unittest.mock import patch
from src.email_utils import send_email

class TestEmailUtils(unittest.TestCase):
    @patch("smtplib.SMTP")
    def test_send_email(self, mock_smtp):
        send_email(
            subject="Test Subject",
            body="Test Body",
            to_email="to@example.com",
            from_email="from@example.com",
            smtp_server="smtp.example.com",
            username="user",
            password="pass"
        )
        mock_smtp.assert_called_with("smtp.example.com", 587)
        instance = mock_smtp.return_value.__enter__.return_value
        instance.starttls.assert_called_once()
        instance.login.assert_called_with("user", "pass")
        instance.sendmail.assert_called()

if __name__ == "__main__":
    unittest.main()
