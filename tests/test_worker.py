from src.infrastructure.database import SessionLocal
from src.data_access.data_accessor import DataAccessor
from src.data_access.repository import SiteRepository
from src.config import config

def test_worker_can_connect_to_db():
    with SessionLocal() as session:
        assert session.is_active

def test_pipeline_transform_and_insert():
    pipeline = DataAccessor(config.SOURCE_ENDPOINT)
    gdf = pipeline.extract()
    transformed = pipeline.transform(gdf)
    
    with SessionLocal() as session:
        repo = SiteRepository(session)
        repo.insert_sites(transformed)
        
        sites = repo.get_all_sites()
        assert len(sites) > 0
        
        for site in sites:
            assert site.country_code is not None
