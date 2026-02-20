import unittest
from src.random_api_webhook import random_api_webhook

class TestRandomAPIWebhook(unittest.TestCase):
    def test_random_api_webhook_keys(self):
        webhook = random_api_webhook()
        self.assertIn("webhook_id", webhook)
        self.assertIn("type", webhook)
        self.assertIn("event", webhook)
        self.assertIn("timestamp", webhook)
        self.assertTrue(webhook["type"] in ["order_update", "user_notification", "payment_status", "shipment_tracking"])

if __name__ == "__main__":
    unittest.main()
