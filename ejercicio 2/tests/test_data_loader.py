import pytest
import os
from src.data_loader import DataLoader

def test_load_valid_json(tmp_path):
    file = tmp_path / "sales.json"
    file.write_text('[{"user_id": "101", "date": "2023-01-01", "price": "10", "quantity": "2"}]')
    loader = DataLoader()
    loader.load_files(str(file))
    assert len(loader.get_data()) == 1

def test_get_user_ids_from_multiple_files(tmp_path):
    json_file = tmp_path / "sales1.json"
    csv_file = tmp_path / "sales2.csv"
    json_file.write_text('[{"user_id": "101", "date": "2023-01-01", "price": "10", "quantity": "2"}]')
    csv_file.write_text("user_id,date,price,quantity\n42,2023-01-01,100,1")

    loader = DataLoader()
    user_ids = loader.get_user_ids(str(tmp_path))
    assert user_ids == ["101", "42"]

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

def test_unsupported_file_format(tmp_path, caplog):
    file = tmp_path / "sales.txt"
    file.write_text("some text")
    loader = DataLoader()
    loader.load_files(str(file))
    assert "Unsupported format" in caplog.text

def test_load_json_object_instead_of_list(tmp_path):
    file = tmp_path / "single.json"
    file.write_text('{"user_id": "101", "date": "2023-01-01", "price": "10", "quantity": "2"}')
    loader = DataLoader()
    loader.load_files(str(file))
    assert loader.get_data() == []

def test_load_csv_missing_fields(tmp_path):
    file = tmp_path / "incomplete.csv"
    file.write_text("user_id,date\n101,2023-01-01")
    loader = DataLoader()
    loader.load_files(str(file))
    assert len(loader.get_data()) == 1
    assert "price" not in loader.get_data()[0]

def test_load_all_mixed_files(tmp_path):
    json_file = tmp_path / "sales1.json"
    csv_file = tmp_path / "sales2.csv"
    json_file.write_text('[{"user_id": "101", "date": "2023-01-01", "price": "10", "quantity": "2"}]')
    csv_file.write_text("user_id,date,price,quantity\n42,2023-01-01,100,1")

    loader = DataLoader()
    data = loader.load_all(str(tmp_path))
    assert len(data) == 2
