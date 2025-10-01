import os
import json
import csv
import logging
import os

class DataLoader:
    def __init__(self):
        self.data = []

    def get_user_ids(self, data_folder):
        all_data = self.load_all(data_folder)
        return sorted(set(str(s["user_id"]) for s in all_data))

    def load_all(self, folder_path):
        all_data = []
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            if filename.endswith(".json"):
                all_data.extend(self._load_json(filepath))
            elif filename.endswith(".csv"):
                all_data.extend(self._load_csv(filepath))
        return all_data


    def load_files(self, *file_paths):
        for path in file_paths:
            if not os.path.exists(path):
                logging.error(f"File not found: {path}")
                continue
            try:
                if path.endswith('.json'):
                    self.data.extend(self._load_json(path))
                elif path.endswith('.csv'):
                    self.data.extend(self._load_csv(path))
                else:
                    logging.warning(f"Unsupported format: {path}")
            except Exception as e:
                logging.error(f"Error loading {path}: {e}")


    def _load_json(self, path):
        try:
            with open(path, "r") as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except Exception as e:
            logging.warning(f"Error loading JSON {path}: {e}")
            return []


    def _load_csv(self, path):
        try:
            with open(path, newline="") as f:
                reader = csv.DictReader(f)
                return list(reader)
        
        except Exception as e:
            logging.warning(f"Error loading CSV {path}: {e}")
            return []


    def get_data(self):
        return self.data
