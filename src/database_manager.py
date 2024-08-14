from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweets'
    
    id = Column(String, primary_key=True)
    text = Column(String)
    created_at = Column(DateTime)

class DatabaseManager:
    def __init__(self, db_path='sqlite:///tweets.db'):
        self.engine = create_engine(db_path, echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def add_tweets(self, tweets, session):
        session.bulk_save_objects(tweets)
        session.commit()