import unittest
import os
import pandas as pd
import sqlite3
from pipeline import main

class TestDataPipeline(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Running the main function 
        main()

    def test_csv_file_exists(self):
        # Check if the CSV exist
        self.assertTrue(os.path.isfile('../data/final_merge_data.csv'), "CSV output file does not exist")

    def test_csv_file_content(self):
        # Load the CSV file and checking the data of this CSV file
        df = pd.read_csv('../data/final_merge_data.csv')
        self.assertFalse(df.empty, "CSV file is empty")
        self.assertTrue(len(df) > 0, "CSV file has no data rows")


if __name__ == '__main__':
    unittest.main()