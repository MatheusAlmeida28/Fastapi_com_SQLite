from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import create_engine


engine=create_engine("sqlite:///games_registry.db",
    echo=True               
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)