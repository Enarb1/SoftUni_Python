from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Relationship

CONNECTION_STRING = 'postgresql+psycopg2://postgres:postgres@localhost:5432/orm_22'
engine = create_engine(CONNECTION_STRING)

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'), default=1)
    city = Relationship('City', backref='users')

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))


Base.metadata.create_all(engine)
