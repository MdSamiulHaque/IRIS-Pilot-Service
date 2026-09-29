import os

class Config:
    REGION = os.getenv("REGION", "EU")
    COUNTRY = os.getenv("COUNTRY", "DE")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5432")
    DB_USER = os.getenv("DB_USER", "iris_user")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "iris_pass")
    DB_NAME = os.getenv("DB_NAME", "iris_db")
    OUTPUT_PATH = os.getenv("OUTPUT_PATH", "./output")
    SOURCE_ENDPOINT = os.getenv("SOURCE_ENDPOINT", "./data/fixtures.geojson")
    
    @property
    def db_url(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

config = Config()
