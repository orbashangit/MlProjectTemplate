import logging
import logging.config
import yaml
import os

def setup_logging(default_path='configs/logging.yaml', default_level=logging.INFO):
    """
    Setup logging configuration from a YAML file.

    Args:
        default_path (str): Path to the logging configuration file.
        default_level (int): Default logging level.
    """
    if os.path.exists(default_path):
        with open(default_path, 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
