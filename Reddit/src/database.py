from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import sessionmaker
import sqlalchemy.exc

Base = declarative_base()

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(String, primary_key=True)
    title = Column(String)
    text = Column(String)
    created_at = Column(String)
    author = Column(String)
    subreddit_name = Column(String)
    score = Column(String)
    url = Column(String)
    

class Database:
    def __init__(self, db_path='sqlite:///posts.db'):
        self.engine = create_engine(db_path, echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
    
    def add_posts(self, posts, session):
        for post in posts:
            try:
                session.add(post)
                session.commit()
            except sqlalchemy.exc.IntegrityError:
                session.rollback()