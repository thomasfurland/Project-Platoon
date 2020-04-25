import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database 
import json
from sqlalchemy.orm import sessionmaker
import psycopg2

Base = declarative_base()
project_dir = os.path.dirname(os.path.abspath(__file__))
engine = create_engine("sqlite:///{}".format(os.path.join(project_dir, 'database.db')), echo=True)
if not database_exists(engine.url):
    create_database(engine.url)

Session = sessionmaker(bind=engine)
session = Session()


class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    points = Column(Integer)

    def create(self):      
        session.add(self)
        session.commit()

    def update(self):
        session.commit()
   

Base.metadata.create_all(engine)

