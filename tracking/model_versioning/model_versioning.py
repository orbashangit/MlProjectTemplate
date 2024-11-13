import os
import joblib

class ModelVersioning:
    def __init__(self, model_path):
        self.model_path = model_path

    def save_model_version(self, model, version):
        """Save the model version."""
        versioned_model_path = os.path.join(self.model_path, f"model_v{version}.pkl")
        joblib.dump(model, versioned_model_path)