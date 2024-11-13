from src.pipeline.evaluator import Evaluator
from src.utils.utils import load_config

class EvaluationPipeline:
    def __init__(self, config_path):
        self.config = load_config(config_path)
        self.evaluator = Evaluator(config_path)

    def run(self):
        # Load processed data
        processed_data = pd.read_csv(self.config['data']['processed_data_path'])
        # Evaluate model
        self.evaluator.evaluate_model(processed_data)

if __name__ == "__main__":
    pipeline = EvaluationPipeline('config/config.yaml')
    pipeline.run()