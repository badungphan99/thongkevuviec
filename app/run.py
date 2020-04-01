from app import *
from app.model import *
from app.controller.Incident import insert_incident, check_incident, update_incident, get_incident_field, get_incident_id, delete_incident
from app.controller.Export import *
from app.View.MainWindows import *

def migrate_db():
    Base.metadata.create_all(engine)

# incident = Incident("1","2","3","4","5")
# insert = db.insert(Incident).values(location = "1", result = "2", reason = "2", solution= "3", fields = "4")
# result = connection.execute(insert)

# insert_incident("2", "4", "5", "4", "bd")

# #
# results = session.execute(db.select([Incident])).fetchall()
# print(results)
#
# print(check_incident(5))

# update_incident(4, "sdsdsd", "sdsdsd", "sdsdsd", "4", "qlsna")
#
# results = session.execute(db.select([Incident])).fetchall()
# print(results)

# print(get_incident_id(4).id)

# get_incident_field("5")

# for incident in incidents:
#     print(incident.id)
# def show_all():
#     incidents = session.query(Incident).all()
#     for incident in incidents:
#         print(incident.id, incident.time, incident.reason, incident.solution, incident.result, incident.location, incident.fields)
#
# # show_all()
# # print(update_incident(2,"1","2","3","4","5"))
# # print(delete_incident(5))
# incidents = get_incident_field("qlsna")
# for incident in incidents:
#     print(incident.id, incident.time, incident.reason, incident.solution, incident.result, incident.location,
#           incident.fields)
# show_all()

# export()
if __name__ == "__main__" :
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec_()
    # migrate_db()