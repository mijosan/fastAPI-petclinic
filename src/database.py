import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from elasticsearch import Elasticsearch

load_dotenv()  # .env 파일에서 환경 변수를 불러옵니다

# SQLAlchemy 설정
RELATION_DATABASE_URL = os.getenv("RELATION_DATABASE_URL")
engine = create_engine(RELATION_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# elasticsearch 설정
ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL")
es_client = Elasticsearch(
    [ELASTICSEARCH_URL]
)

def get_rdb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_es():
    return es_client
