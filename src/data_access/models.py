from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from geoalchemy2 import Geometry
from src.infrastructure.database import Base

class ProspectiveSite(Base):
    __tablename__ = "prospective_sites"
    
    id = Column(Integer, primary_key=True, index=True)
    site_name = Column(String, nullable=True)
    eco_points_per_m2 = Column(Float, nullable=True)
    country_code = Column(String, nullable=False)
    geom = Column(Geometry('POINT', srid=4326), nullable=True)
    site_suitability = Column(Boolean, nullable=True)
    source_date = Column(DateTime, nullable=True)
    uncertainty = Column(String, default="not provided")
