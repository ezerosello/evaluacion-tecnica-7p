import pytest
from sqlalchemy import create_engine, func, case, cast, Float
from sqlalchemy.orm import sessionmaker
from models import Base, Country, Capital
from datetime import datetime, timezone
from fastapi.testclient import TestClient
from app import app
import requests


@pytest.fixture(scope="function")
def test_db():
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()

# persistencia de países desde API externa
def test_load_countries_persistence(test_db):
    # Simular datos externos
    sample_data = [
        {
            "name": {"common": "Testland"},
            "region": "TestRegion",
            "population": 123456,
            "area": 789.0,
            "cca2": "TL",
            "capital": ["Testville"]
        }
    ]

    # Simular carga
    for item in sample_data:
        country = Country(
            name=item["name"]["common"],
            region=item["region"],
            population=item["population"],
            area=item["area"],
            code=item["cca2"],
            capital=item["capital"][0]
        )
        test_db.add(country)
    test_db.commit()

    # Verificar persistencia
    result = test_db.query(Country).filter_by(name="Testland").first()
    assert result is not None
    assert result.region == "TestRegion"
    assert result.population == 123456

# persistencia de capitales
def test_populate_capitals_persistence(test_db):
    country = Country(
        name="Testland",
        region="TestRegion",
        population=100000,
        area=500.0,
        code="TL",
        capital="Testville"
    )
    test_db.add(country)
    test_db.commit()

    capital = Capital(
        name="Testville",
        temperature=25.0,
        humidity=60,
        last_updated=datetime.now(timezone.utc),
        country_id=country.id
    )
    test_db.add(capital)
    test_db.commit()

    result = test_db.query(Capital).filter_by(name="Testville").first()
    assert result is not None
    assert result.temperature == 25.0
    assert result.country.name == "Testland"


def test_country_stats_density(test_db):
    # Cargar países con población y área
    test_db.add_all([
        Country(name="A", region="X", population=1000, area=100.0, code="A", capital="A-Cap"),
        Country(name="B", region="X", population=2000, area=200.0, code="B", capital="B-Cap"),
        Country(name="C", region="Y", population=3000, area=150.0, code="C", capital="C-Cap"),
    ])
    test_db.commit()

    # Calcular densidad promedio por región
    results = (
        test_db.query(
            Country.region,
            func.avg(
                case(
                    (Country.area != None, Country.population / cast(Country.area, Float)),
                    else_=None
                )
            ).label("average_density")
        )
        .group_by(Country.region)
        .all()
    )

    assert len(results) == 2
    for region, avg in results:
        assert avg > 0
