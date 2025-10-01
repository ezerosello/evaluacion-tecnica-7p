import pytest
import os
from src.data_loader import DataLoader

def test_load_valid_json(tmp_path):
    file = tmp_path / "sales.json"
    file.write_text('[{"user_id": "101", "date": "2023-01-01", "price": "10", "quantity": "2"}]')
    loader = DataLoader()
    loader.load_files(str(file))
    assert len(loader.get_data()) == 1

def test_load_invalid_json(tmp_path, caplog):
    file = tmp_path / "bad.json"
    file.write_text('not a json')
    loader = DataLoader()
    loader.load_files(str(file))
    assert "Error loading" in caplog.text

def test_load_valid_csv(tmp_path):
    file = tmp_path / "sales.csv"
    file.write_text("user_id,date,price,quantity\n101,2023-01-01,10,2")
    loader = DataLoader()
    loader.load_files(str(file))
    assert len(loader.get_data()) == 1

def test_file_not_found(caplog):
    loader = DataLoader()
    loader.load_files("nonexistent.json")
    assert "File not found" in caplog.text
