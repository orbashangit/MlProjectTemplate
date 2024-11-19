import pandas as pd
from src.models.xgboost_model import XGBoostModel
import logging

class Predictor:
    """
    Class for making predictions with the trained model.
    """

    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        self.model = XGBoostModel(config)
        # Load the trained model
        self.model.model.load_model('models/xgboost_model.json')

    def predict(self, X: pd.DataFrame) -> pd.Series:
        """
        Make predictions on new data.

        Args:
            X (pd.DataFrame): Features.

        Returns:
            pd.Series: Predicted labels.
        """
        self.logger.info("Making predictions")
        predictions = self.model.model.predict(X)
        return predictions
