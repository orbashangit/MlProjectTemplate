from src.data.data_loader import DataLoader
from src.data.data_cleaner import DataCleaner
from src.utils.utils import load_config

class DataPreprocessingPipeline:
    def __init__(self, config_path):
        self.config = load_config(config_path)
        self.data_loader = DataLoader(config_path)
        self.data_cleaner = DataCleaner()

    def run(self):
        # Load raw data
        raw_data = self.data_loader.load_csv(self.config['data']['raw_data_path'])
        # Clean data
        cleaned_data = self.data_cleaner.clean_data(raw_data)
        # Feature engineering
        processed_data = self.data_cleaner.feature_engineering(cleaned_data)
        # Save processed data
        processed_data.to_csv(self.config['data']['processed_data_path'], index=False)

if __name__ == "__main__":
    pipeline = DataPreprocessingPipeline('config/config.yaml')
    pipeline.run()