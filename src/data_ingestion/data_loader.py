import pandas as pd
import pyodbc
import yaml

class DataLoader:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)

    def load_csv(self, file_path):
        """Load data from a CSV file."""
        return pd.read_csv(file_path)

    def load_mssql(self, query):
        """Load data from MSSQL database."""
        conn = pyodbc.connect(self.config['database']['connection_string'])
        return pd.read_sql(query, conn)