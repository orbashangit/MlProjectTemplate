import os
import pandas as pd
import hashlib

class DataVersioning:
    def __init__(self, data_path):
        self.data_path = data_path

    def get_file_hash(self, file_path):
        """Generate a hash for the given file."""
        hasher = hashlib.md5()
        with open(file_path, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

    def log_data_version(self, file_path):
        """Log the version of the data file."""
        file_hash = self.get_file_hash(file_path)
        log_entry = f"{file_path}: {file_hash}\n"
        with open(os.path.join(self.data_path, 'data_version.log'), 'a') as log_file:
            log_file.write(log_entry)