from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Incident(Base):
    __tablename__= 'incident'
    id = Column(Integer, primary_key = True)
    time = Column(String)
    location = Column(String)
    result = Column(String)
    reason = Column(String)
    solution = Column(String)
    fields = Column(String)
    time_modify = Column(DateTime)

    def __init__(self, time, location, result, reason, solution, fields, time_modify):
        self.time = time
        self.location = location
        self.result = result
        self.reason = reason
        self.solution = solution
        self.fields = fields
        self.time_modify = time_modify
