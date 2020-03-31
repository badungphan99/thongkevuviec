import csv

from app.model import *
from app import session

def export():
    outfile = open('./mydump.csv', 'w')
    outcsv = csv.writer(outfile)

    incidents = session.query(Incident).all()

    # dump column titles (optional)
    outcsv.writerow(["id", "time", "location", "result", "reason", "solution", "fields", "time modify"])
    # dump rows
    for incident in incidents:
        outcsv.writerow([str(incident.id), incident.time, incident.location, incident.result, incident.reason, incident.solution, incident.fields])

    outfile.close()