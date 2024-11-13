from src.pipeline.trainer import Trainer
from src.utils.utils import load_config

class TrainingPipeline:
    def __init__(self, config_path):
        self.config = load_config(config_path)
        self.trainer = Trainer(config_path)

    def run(self):
        # Load processed data
        processed_data = pd.read_csv(self.config['data']['processed_data_path'])
        # Train model
        self.trainer.train_model(processed_data)

if __name__ == "__main__":
    pipeline = TrainingPipeline('config/config.yaml')
    pipeline.run()