import csv

from app.model import *
from app import session

def export(incidents, path):
    outfile = open(path, 'w')
    outcsv = csv.writer(outfile)
    # dump column titles (optional)
    outcsv.writerow(["Id", "Thời gian", "Địa điểm", "Kết quả", "Lý do", "Giải pháp", "Lĩnh vực", "Thời gian chỉnh sửa"])
    # dump rows
    for incident in incidents:
        outcsv.writerow([str(incident.id), incident.time, incident.location, incident.result, incident.reason, incident.solution, incident.fields, incident.time_modify])
    outfile.close()