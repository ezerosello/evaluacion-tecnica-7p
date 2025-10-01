import pytest
import os
import json
from src.report_generator import ReportGenerator

sample_report = {
    "user_id": "101",
    "monthly": {"2023-01": {"total": 20, "count": 1, "average": 20}},
    "yearly": {"2023": {"total": 20, "count": 1, "average": 20}},
    "generated_at": "2023-10-01T00:00:00"
}

def test_export_json(tmp_path):
    generator = ReportGenerator({'output_type': 'json'})
    generator.export(sample_report, tmp_path)
    file = tmp_path / "sales_report_101.json"
    assert file.exists()
    assert json.loads(file.read_text())["user_id"] == "101"

def test_export_csv(tmp_path):
    generator = ReportGenerator({'output_type': 'csv'})
    generator.export(sample_report, tmp_path)
    file = tmp_path / "sales_report_101.csv"
    assert file.exists()
    assert "Period,Total,Average,Count" in file.read_text()

def test_export_unsupported_format(caplog, tmp_path):
    generator = ReportGenerator({'output_type': 'xml'})
    generator.export(sample_report, tmp_path)
    assert "Unsupported format" in caplog.text

def test_export_incomplete_report(caplog, tmp_path):
    generator = ReportGenerator()
    generator.export({"user_id": "101"}, tmp_path)
    assert "Incomplete report structure" in caplog.text
