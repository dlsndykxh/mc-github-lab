import unittest
from optimizer import average_mspt, overloaded


class OptimizerTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(average_mspt([10, 20, 30]), 20)

    def test_empty_samples_rejected(self):
        with self.assertRaises(ValueError):
            average_mspt([])

    def test_overloaded(self):
        self.assertTrue(overloaded([45, 65]))

    def test_normal(self):
        self.assertFalse(overloaded([30, 40]))

    def test_budget_boundary(self):
        self.assertFalse(overloaded([50, 50]))


if __name__ == "__main__":
    unittest.main()
