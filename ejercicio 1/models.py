from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    population = Column(Integer, nullable=False)
    area = Column(Float, nullable=True)
    code = Column(String, unique=True, nullable=False)
    capital = Column(String, nullable=True)

    cities = relationship("Capital", back_populates="country")


class Capital(Base):
    __tablename__ = "capitals"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    temperature = Column(Float, nullable=True)
    humidity = Column(Integer, nullable=True)
    last_updated = Column(DateTime, nullable=True)
    country_id = Column(Integer, ForeignKey("countries.id"))

    country = relationship("Country", back_populates="cities")