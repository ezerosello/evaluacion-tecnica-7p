from fastapi import FastAPI, Depends, Query
from sqlalchemy import func
from sqlalchemy.orm import Session
from init_db import init_db, load_countries
from database import SessionLocal
from models import Country
from contextlib import asynccontextmanager
from typing import Optional

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    load_countries()
    print("Database initialized and countries loaded.")
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


from fastapi import HTTPException

@app.get("/countries/stats")
def get_country_stats(metric: str, db: Session = Depends(get_db)):
    if metric not in ["population", "area"]:
        raise HTTPException(status_code=400, detail="Metric must be 'population' or 'area'")

    # Selección dinámica de columna
    column = getattr(Country, metric)

    # Consulta agregada: promedio por región
    results = (
        db.query(
            Country.region,
            func.avg(column).label(f"average_{metric}")
        )
        .group_by(Country.region)
        .all()
    )

    # Transformar a lista de dicts
    return [
        {"region": region, f"average_{metric}": round(avg, 2) if avg else None}
        for region, avg in results
    ]
