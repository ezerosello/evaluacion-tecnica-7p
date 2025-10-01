import os
import json
import csv
import logging

class DataLoader:
    def __init__(self):
        self.data = []

    def load_files(self, *file_paths):
        for path in file_paths:
            if not os.path.exists(path):
                logging.error(f"File not found: {path}")
                continue
            try:
                if path.endswith('.json'):
                    self._load_json(path)
                elif path.endswith('.csv'):
                    self._load_csv(path)
                else:
                    logging.warning(f"Unsupported format: {path}")
            except Exception as e:
                logging.error(f"Error loading {path}: {e}")

    def _load_json(self, path):
        with open(path, encoding='utf-8') as f:
            content = json.load(f)
            if isinstance(content, list):
                self.data.extend(content)
            else:
                logging.warning(f"Invalid JSON format in {path}")

    def _load_csv(self, path):
        with open(path, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            self.data.extend(list(reader))

    def get_data(self):
        return self.data
