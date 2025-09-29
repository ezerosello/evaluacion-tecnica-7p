from models import Base
from database import engine, SessionLocal
import requests
from models import Country

def init_db():
    Base.metadata.create_all(bind=engine)

def load_countries():
    url = "https://restcountries.com/v3.1/all?fields=name,region,population,area"
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

        if not name or not region or population is None:
            continue

        exists = db.query(Country).filter_by(name=name).first()
        if exists:
            continue

        country = Country(
            name=name,
            region=region,
            population=population,
            area=area
        )
        db.add(country)

    db.commit()
    db.close()
