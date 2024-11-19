import xgboost as xgb
import logging

class XGBoostModel:
    """
    XGBoost model for classification.
    """

    def __init__(self, config: dict):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        self.model = xgb.XGBClassifier(**self.config['model']['xgboost']['params'])

    def train(self, X_train, y_train):
        """
        Train the XGBoost model.

        Args:
            X_train (pd.DataFrame): Training features.
            y_train (pd.Series): Training labels.
        """
        self.logger.info("Training XGBoost model")
        self.model.fit(X_train, y_train)

    def evaluate(self, X_test, y_test):
        """
        Evaluate the XGBoost model.

        Args:
            X_test (pd.DataFrame): Test features.
            y_test (pd.Series): Test labels.

        Returns:
            float: Test accuracy.
        """
        self.logger.info("Evaluating XGBoost model")
        accuracy = self.model.score(X_test, y_test)
        return accuracy
