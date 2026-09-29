from src.infrastructure.database import SessionLocal
from src.data_access.repository import SiteRepository
from src.data_access.data_accessor import DataAccessor
from src.config import config

def main():
    pipeline = DataAccessor(config.SOURCE_ENDPOINT)
    gdf = pipeline.extract()
    transformed_data = pipeline.transform(gdf)
    
    with SessionLocal() as session:
        repo = SiteRepository(session)
        repo.insert_sites(transformed_data)
        
if __name__ == "__main__":
    main()
