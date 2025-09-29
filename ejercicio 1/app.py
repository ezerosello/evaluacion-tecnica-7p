from contextlib import asynccontextmanager
from database import SessionLocal
from fastapi import FastAPI, Depends, Query, HTTPException
from init_db import init_db, load_countries
from models import Country
from sqlalchemy import func, case, cast, Float
from sqlalchemy.orm import Session
from typing import Optional


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    load_countries()
    yield

app = FastAPI(lifespan=lifespan)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/countries")
def read_countries(region: Optional[str] = Query(None), db: Session = Depends(get_db)):
    if region:
        countries = db.query(Country).filter(Country.region == region).all()
    else:
        countries = db.query(Country).all()
    return countries


@app.get("/countries/stats")
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
            {"region": region, f"average_{metric}": round(avg, 2) if avg else None}
            for region, avg in results
        ]

    elif metric == "density":
        # Evitar división por cero o NULL
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
            {"region": region, "average_density": round(density, 2) if density else None}
            for region, density in results
        ]

    elif metric == "max_population":
        subquery = (
            db.query(
                Country.region,
                func.max(Country.population).label("max_pop")
            )
            .group_by(Country.region)
            .subquery()
        )

        results = (
            db.query(Country.region, Country.name, Country.population)
            .join(subquery, (Country.region == subquery.c.region) & (Country.population == subquery.c.max_pop))
            .all()
        )

        return [
            {"region": region, "country": name, "population": population}
            for region, name, population in results
        ]

    else:
        raise HTTPException(
            status_code=400,
            detail="Metric must be one of: 'population', 'area', 'density', 'max_population'"
        )

