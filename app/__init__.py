from sqlalchemy import create_engine

engine = create_engine('sqlite:///dungpb.sqlite')

connecrtion = engine.connect()