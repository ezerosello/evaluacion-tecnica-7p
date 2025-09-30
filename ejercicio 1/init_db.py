from models import Base, Country, Capital
from database import engine, SessionLocal
from datetime import datetime, timezone
import requests

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

from datetime import datetime, timezone
from requests.utils import quote

def populate_capitals(api_key: str):
    if not api_key:
        raise RuntimeError("API_KEY no está definida en el entorno")

    db = SessionLocal()
    countries = db.query(Country).filter(Country.capital != None).all()

    for country in countries:
        capital_name = country.capital
        url = f"https://api.openweathermap.org/data/2.5/weather?q={quote(capital_name)}&appid={api_key}&units=metric"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"No se encontró la capital {capital_name}: {response.status_code} - {response.text}")
            continue

        data = response.json()
        temp = data.get("main", {}).get("temp")
        humidity = data.get("main", {}).get("humidity")

        if temp is None or humidity is None:
            print(f"⚠️ Datos incompletos para {capital_name}: temp={temp}, humidity={humidity}")
            continue

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
