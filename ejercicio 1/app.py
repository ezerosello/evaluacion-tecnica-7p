from contextlib import asynccontextmanager
from database import SessionLocal
from fastapi import FastAPI, Depends, Query, HTTPException, Path
from init_db import init_db, load_countries, populate_capitals
from models import Country, Capital
from schemas import CapitalOut, WeatherOut, CountryOut, RegionStat
from sqlalchemy import func, case, cast, Float
from sqlalchemy.orm import Session
from typing import Optional, List

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    load_countries()
    populate_capitals(api_key="9a4e499d3f7bc641d86290a592416c6b")
    yield

app = FastAPI(lifespan=lifespan)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/countries", response_model=List[CountryOut])
def get_countries(region: Optional[str] = Query(None), db: Session = Depends(get_db)):
    if region:
        countries = db.query(Country).filter(Country.region == region).all()
        if not countries:
            raise HTTPException(status_code=404, detail=f"No se encontraron países en la región '{region}'")
    else:
        countries = db.query(Country).all()
    return countries


@app.get("/countries/stats", response_model=List[RegionStat])
def get_country_stats(metric: str, db: Session = Depends(get_db)):
    if metric in ["population", "area"]:
        column = getattr(Country, metric)

        results = (
            db.query(
                Country.region,
                func.avg(column).label(f"average_{metric}")
            )
            .group_by(Country.region)
            .all()
        )

        return [
            RegionStat(region=region, value=round(avg, 2) if avg else None)
            for region, avg in results
        ]

    elif metric == "density":

        results = (
            db.query(
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

        return [
            RegionStat(region=region, value=round(avg, 2) if avg else None)
            for region, avg in results
        ]

    else:
        raise HTTPException(
            status_code=400,
            detail="Metric must be one of: 'population', 'area', 'density'"
        )
    
    
@app.get("/capitals", response_model=List[CapitalOut])
def get_capitals(db: Session = Depends(get_db)):
    capitals = db.query(Capital).join(Country).all()
    result = []
    for capital in capitals:
        result.append(CapitalOut(
            id=capital.id,
            name=capital.name,
            temperature=capital.temperature,
            humidity=capital.humidity,
            last_updated=capital.last_updated.isoformat() if capital.last_updated else None,
            country_name=capital.country.name,
            country_code=capital.country.code
        ))
    return result


@app.get("/weather/{city}", response_model=WeatherOut)
def get_capital_weather(city: str, db: Session = Depends(get_db)):
    capital = db.query(Capital).filter(Capital.name.ilike(city)).first()

    if not capital:
        raise HTTPException(status_code=404, detail=f"{city} no está en la base de datos")

    return WeatherOut(
        city=capital.name,
        temperature=capital.temperature,
        humidity=capital.humidity,
        last_updated=capital.last_updated.isoformat() if capital.last_updated else None
    )