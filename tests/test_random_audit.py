import unittest
from src.random_audit import random_audit_record

class TestRandomAudit(unittest.TestCase):
    def test_random_audit_record_keys(self):
        audit = random_audit_record()
        self.assertIn("audit_id", audit)
        self.assertIn("user", audit)
        self.assertIn("action", audit)
        self.assertIn("timestamp", audit)
        self.assertTrue(audit["action"] in ["create", "update", "delete", "access", "login"])

if __name__ == "__main__":
    unittest.main()
