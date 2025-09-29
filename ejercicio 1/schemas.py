from pydantic import BaseModel, ConfigDict
from typing import Optional

class CountryOut(BaseModel):
    id: int
    name: str
    region: str
    population: int
    area: Optional[float]
    code: str
    capital: Optional[str]

    model_config = ConfigDict(from_attributes=True)

class RegionStat(BaseModel):
    region: str
    value: Optional[float]

    model_config = ConfigDict(from_attributes=True)

class CapitalOut(BaseModel):
    id: int
    name: str
    temperature: Optional[float]
    humidity: Optional[int]
    last_updated: Optional[str]
    country_name: str
    country_code: str

    model_config = ConfigDict(from_attributes=True)

class WeatherOut(BaseModel):
    city: str
    temperature: Optional[float]
    humidity: Optional[int]
    last_updated: Optional[str]

    model_config = ConfigDict(from_attributes=True)
