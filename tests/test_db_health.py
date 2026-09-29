from src.infrastructure.database import engine
from sqlalchemy import text

def test_db_starts_and_healthy():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        assert result.scalar() == 1
