import pandas as pd
from sklearn.metrics import classification_report
import logging

class Evaluator:
    """
    Class for evaluating model performance.
    """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def evaluate(self, y_true, y_pred):
        """
        Evaluate the model predictions.

        Args:
            y_true (pd.Series): True labels.
            y_pred (pd.Series): Predicted labels.

        Returns:
            dict: Classification report.
        """
        self.logger.info("Evaluating model predictions")
        report = classification_report(y_true, y_pred, output_dict=True)
        self.logger.info(f"Classification Report: {report}")
        return report
