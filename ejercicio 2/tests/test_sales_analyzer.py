import pytest
import logging
from src.sales_analyzer import SalesAnalyzer

sample_data = [
    {"user_id": "101", "date": "2023-01-01", "price": "10", "quantity": "2"},
    {"user_id": "101", "date": "2023-02-01", "price": "20", "quantity": "1"},
    {"user_id": "102", "date": "invalid", "price": "30", "quantity": "1"},
]

def test_analyze_valid_user():
    analyzer = SalesAnalyzer(sample_data)
    assert analyzer.analyze_user("101") is True
    report = analyzer.get_report("101")
    assert report is not None
    assert "monthly" in report and "yearly" in report
    assert report["user_id"] == "101"

def test_analyze_invalid_user(caplog):
    caplog.set_level(logging.INFO)
    analyzer = SalesAnalyzer(sample_data)
    assert analyzer.analyze_user("999") is False
    assert "No sales for user 999" in caplog.text
    assert analyzer.get_report("999") is None

def test_analyze_user_with_invalid_record(caplog):
    caplog.set_level(logging.WARNING)
    analyzer = SalesAnalyzer(sample_data)
    analyzer.analyze_user("102")
    assert "Invalid record after coercion" in caplog.text

def test_missing_fields_logged(caplog):
    caplog.set_level(logging.WARNING)
    data = [
        {"user_id": "103", "date": "2023-03-01", "price": "15"},  # falta quantity
        {"user_id": "103", "price": "15", "quantity": "2"},       # falta date
    ]
    analyzer = SalesAnalyzer(data)
    analyzer.analyze_user("103")
    assert "Missing fields in record" in caplog.text

def test_all_records_invalid(caplog):
    caplog.set_level(logging.INFO)
    data = [
        {"user_id": "104", "date": "invalid", "price": "bad", "quantity": "none"},
        {"user_id": "104", "date": None, "price": None, "quantity": None},
    ]
    analyzer = SalesAnalyzer(data)
    result = analyzer.analyze_user("104")
    assert result is False
    assert "All records for user 104 were invalid after coercion" in caplog.text
    assert analyzer.get_report("104") is None

def test_mixed_valid_and_invalid_records(caplog):
    caplog.set_level(logging.WARNING)
    data = [
        {"user_id": "105", "date": "2023-04-01", "price": "25", "quantity": "2"},
        {"user_id": "105", "date": "invalid", "price": "25", "quantity": "2"},
        {"user_id": "105", "price": "25", "quantity": "2"},  # falta date
    ]
    analyzer = SalesAnalyzer(data)
    result = analyzer.analyze_user("105")
    assert result is True
    report = analyzer.get_report("105")
    assert report is not None
    assert "monthly" in report
    assert "Invalid record" in caplog.text or "Missing fields in record" in caplog.text
