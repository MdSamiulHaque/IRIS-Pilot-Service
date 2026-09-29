from src.infrastructure.database import engine, Base
from sqlalchemy import text
import src.data_access.models

def run_migrations():
    with engine.connect() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS postgis;"))
        conn.commit()
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    run_migrations()
