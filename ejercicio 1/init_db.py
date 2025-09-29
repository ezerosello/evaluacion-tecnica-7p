from models import Base, Country, Capital
from database import engine, SessionLocal
from datetime import datetime, timezone
import requests
import os

def init_db():
    Base.metadata.create_all(bind=engine)

def load_countries():
    url = "https://restcountries.com/v3.1/all?fields=name,region,population,area,cca2,capital"
    response = requests.get(url)
    data = response.json()

    db = SessionLocal()

    for item in data:
        if not isinstance(item, dict):
            continue

        name = item.get("name", {}).get("common")
        region = item.get("region")
        population = item.get("population")
        area = item.get("area")
        code = item.get("cca2")
        capital_list = item.get("capital", [])
        capital = capital_list[0] if capital_list else None

        if db.query(Country).filter(Country.name == name).first():
            continue

        if not name or not region or population is None:
            continue

        exists = db.query(Country).filter_by(name=name).first()
        if exists:
            continue

        country = Country(
            name=name,
            region=region,
            population=population,
            area=area,
            code=code,
            capital=capital
        )
        db.add(country)

    db.commit()
    db.close()

def populate_capitals(api_key: str):
    db = SessionLocal()
    countries = db.query(Country).filter(Country.capital != None).all()

    for country in countries:
        capital_name = country.capital
        url = f"https://api.openweathermap.org/data/2.5/weather?q={capital_name}&appid={api_key}&units=metric"
        response = requests.get(url)

        data = response.json()
        temp = data.get("main", {}).get("temp")
        humidity = data.get("main", {}).get("humidity")

        # Evitar duplicados
        if db.query(Capital).filter_by(name=capital_name, country_id=country.id).first():
            continue

        capital = Capital(
            name=capital_name,
            temperature=temp,
            humidity=humidity,
            last_updated=datetime.now(timezone.utc),
            country_id=country.id
        )
        db.add(capital)

    db.commit()
    db.close()