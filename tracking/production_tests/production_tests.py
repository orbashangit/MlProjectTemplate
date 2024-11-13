import os
import pandas as pd
from sklearn.metrics import classification_report

class ProductionTests:
    def __init__(self, model, test_data_path):
        self.model = model
        self.test_data_path = test_data_path

    def run_production_tests(self):
        """Run production tests on the model."""
        test_data = pd.read_csv(self.test_data_path)
        X_test = test_data.drop('target', axis=1)
        y_test = test_data['target']
        y_pred = self.model.predict(X_test)
        report = classification_report(y_test, y_pred)
        print(report)
        with open(os.path.join(self.test_data_path, 'production_test_report.txt'), 'w') as report_file:
            report_file.write(report)