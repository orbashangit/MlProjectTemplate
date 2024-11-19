import unittest
import os
from src.data_ingestion.data_loader import DataLoader
from src.utils.config_loader import load_config

class TestDataLoader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config = load_config('configs/config.yaml')
        cls.data_loader = DataLoader(cls.config)

    def test_load_from_csv(self):
        df = self.data_loader.load_from_csv('sample.csv')
        self.assertFalse(df.empty)

    def test_load_from_database(self):
        # Assuming a test database and table exist
        query = "SELECT TOP 10 * FROM test_table"
        df = self.data_loader.load_from_database(query)
        self.assertFalse(df.empty)

if __name__ == '__main__':
    unittest.main()
