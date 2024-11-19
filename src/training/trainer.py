import pandas as pd
from sklearn.model_selection import train_test_split
from src.models.xgboost_model.py import XGBoostModel
import logging

class Trainer:
    """
    Class to orchestrate the training process.
    """

    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        self.model = XGBoostModel(config)

    def train(self, X: pd.DataFrame, y: pd.Series):
        """
        Train the model.

        Args:
            X (pd.DataFrame): Features.
            y (pd.Series): Labels.
        """
        self.logger.info("Starting training process")
        X_train, X_val, y_train, y_val = train_test_split(
            X, y,
            test_size=self.config['data']['test_size'],
            random_state=self.config['data']['random_state']
        )
        self.model.train(X_train, y_train)
        accuracy = self.model.evaluate(X_val, y_val)
        self.logger.info(f"Validation Accuracy: {accuracy}")
