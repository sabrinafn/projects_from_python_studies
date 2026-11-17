from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_dir = Path(__file__).resolve().parents[1] / "database"
db_dir.mkdir(exist_ok=True)

engine = create_engine(
    f"sqlite:///{db_dir / 'journal.db'}",
    connect_args={"check_same_thread": False},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

Base = declarative_base()