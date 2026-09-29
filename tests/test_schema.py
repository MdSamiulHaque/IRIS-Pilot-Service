from src.infrastructure.database import engine
from sqlalchemy import text

def test_migrations_applied_and_tables_exist():
    with engine.connect() as conn:
        result = conn.execute(text(
            "SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'prospective_sites');"
        ))
        assert result.scalar() is True

def test_geom_column_exists():
    with engine.connect() as conn:
        result = conn.execute(text(
            "SELECT EXISTS (SELECT FROM information_schema.columns WHERE table_name = 'prospective_sites' AND column_name = 'geom');"
        ))
        assert result.scalar() is True
