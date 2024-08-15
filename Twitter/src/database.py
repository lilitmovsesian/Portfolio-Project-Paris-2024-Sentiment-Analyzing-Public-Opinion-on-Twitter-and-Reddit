from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, DateTime
from sqlalchemy.orm import sessionmaker
import sqlalchemy.exc

Base = declarative_base()

class Tweet(Base):
    __tablename__ = 'tweets'
    
    id = Column(String, primary_key=True)
    text = Column(String)
    created_at = Column(DateTime)
    author_id = Column(String)
    name = Column(String)
    username = Column(String)
    location = Column(String)
    verified = Column(String)

class Database:
    def __init__(self, db_path='sqlite:///tweets.db'):
        self.engine = create_engine(db_path, echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
    
    def add_tweets(self, tweets, session):
        for tweet in tweets:
            try:
                session.add(tweet)
                session.commit()
            except sqlalchemy.exc.IntegrityError:
                session.rollback()