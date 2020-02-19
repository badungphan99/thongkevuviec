from sqlalchemy import create_engine
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///dungpb.db', echo = True)
Base = declarative_base()

class Incident(Base):
    __tablename__= 'incident'
    id = Column(Integer, primary_key = True)
    time = Column(DateTime)
    location = Column(String)
    result = Column(String)
    reason = Column(String)
    solution = Column(String)
    fileds = Column(String)

    def __init__(self, time, location, result, reason, solution, fileds):
        self.time = time
        self.location = location
        self.result = result
        self.reason = reason
        self.solution = solution
        self.fileds = fileds

Base.metadata.create_all(engine)