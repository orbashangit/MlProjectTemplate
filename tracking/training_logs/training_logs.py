import logging

class TrainingLogs:
    def __init__(self, log_path):
        self.log_path = log_path
        logging.basicConfig(filename=self.log_path, level=logging.INFO)

    def log_training_progress(self, message):
        """Log training progress."""
        logging.info(message)