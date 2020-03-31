import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

engine = db.create_engine('sqlite:///../Database/dungpb.db', echo = False)
Session = sessionmaker(bind=engine)
session = Session()