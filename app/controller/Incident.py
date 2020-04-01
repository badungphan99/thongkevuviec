import datetime

from app.model import *
from app import session

def insert_incident(time, location, result, reason, solution, fields):
    time_modify = datetime.datetime.now()
    incident1 = Incident(time, location, result, reason, solution, fields, time_modify)
    session.add(incident1)
    session.commit()

def check_incident(id):
    exists = session.query(Incident).filter_by(id=id).scalar()
    session.commit()
    return exists != None

def get_incident_field(field):
    if(field == ""):
        incidents = session.query(Incident).all()
    else:
        incidents = session.query(Incident).filter_by(fields = field).all()
    session.commit()
    return incidents

def get_incident_id(id):
    incident = session.query(Incident).filter_by(id=id).one()
    session.commit()
    return incident

def update_incident(id, time, location, result, reason, solution, fields):
    if(check_incident(id)):
        incident = session.query(Incident).filter_by(id= id).one()
        incident.time = time
        incident.location = location
        incident.result = result
        incident.reason = reason
        incident.solution = solution
        incident.fields = fields
        incident.time_modify = datetime.datetime.now()
        session.commit()
        return True
    else:
        return False

def delete_incident(id):
    if(check_incident(id)):
        incident = get_incident_id(id)
        session.delete(incident)
        session.commit()
        return True
    else:
        return False

def get_all_incident():
    incidents = session.query(Incident).all()
    return incidents