import yaml
import os

def load_config(config_file_path: str) -> dict:
    """
    Load configuration settings from a YAML file.

    Args:
        config_file_path (str): Path to the configuration file.

    Returns:
        dict: Configuration settings.
    """
    with open(config_file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config
