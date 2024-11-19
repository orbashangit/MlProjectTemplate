import pandas as pd
import pyodbc
import logging

class DataLoader:
    """
    Class for loading data from various sources.
    """

    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    def load_from_csv(self, file_name: str) -> pd.DataFrame:
        """
        Load data from a CSV file.

        Args:
            file_name (str): Name of the CSV file.

        Returns:
            pd.DataFrame: Loaded data.
        """
        file_path = os.path.join(self.config['data']['raw_data_path'], file_name)
        self.logger.info(f"Loading data from {file_path}")
        df = pd.read_csv(file_path)
        return df

    def load_from_database(self, query: str) -> pd.DataFrame:
        """
        Load data from a MSSQL database.

        Args:
            query (str): SQL query to execute.

        Returns:
            pd.DataFrame: Loaded data.
        """
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.config['database']['host']},{self.config['database']['port']};"
            f"DATABASE={self.config['database']['database_name']};"
            f"UID={self.config['database']['username']};"
            f"PWD={self.config['database']['password']}"
        )
        self.logger.info("Connecting to the database")
        conn = pyodbc.connect(conn_str)
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
