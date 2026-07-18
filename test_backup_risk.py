import unittest

from backup_risk import classify


class BackupRiskTest(unittest.TestCase):
    def test_critical_failing_backup_is_high_risk(self):
        row = {"job": "crm", "tier": "critical", "hours_since_success": "30", "failures_24h": "2", "encrypted": "yes"}
        self.assertEqual(classify(row), "high")


if __name__ == "__main__":
    unittest.main()
