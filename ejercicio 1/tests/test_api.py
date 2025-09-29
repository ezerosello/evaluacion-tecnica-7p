from fastapi.testclient import TestClient
from app import app
from schemas import CountryOut, CapitalOut, WeatherOut, RegionStat
import pytest

client = TestClient(app)

def test_get_countries_200():
    response = client.get("/countries")
    assert response.status_code == 200
    countries = response.json()
    assert isinstance(countries, list)
    for country in countries:
        CountryOut(**country) 


def test_get_countries_invalid_region():
    response = client.get("/countries?region=Atlantis")
    assert response.status_code == 404 


def test_get_capitals_200():
    response = client.get("/capitals")
    assert response.status_code == 200
    capitals = response.json()
    assert isinstance(capitals, list)
    for capital in capitals:
        CapitalOut(**capital)


def test_get_weather_valid_city():
    response = client.get("/weather/Buenos Aires")
    if response.status_code == 200:
        WeatherOut(**response.json())
    else:
        assert response.status_code == 404


def test_get_weather_invalid_city():
    response = client.get("/weather/Narnia")
    assert response.status_code == 404
    assert "no está en la base de datos" in response.json()["detail"]


@pytest.mark.parametrize("metric", ["population", "area", "density"])
def test_get_country_stats_valid(metric):
    response = client.get(f"/countries/stats?metric={metric}")
    assert response.status_code == 200
    stats = response.json()
    for item in stats:
        RegionStat(**item)


def test_get_country_stats_invalid_metric():
    response = client.get("/countries/stats?metric=max_population")
    assert response.status_code == 400
    assert "Metric must be one of" in response.json()["detail"]
