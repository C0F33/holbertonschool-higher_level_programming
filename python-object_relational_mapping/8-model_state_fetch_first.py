#!/usr/bin/python3
"""fetch fist state in db"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost//\
                           {}'.format(argv[1], argv[2],argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first_state = session.query(State).order_by(State.id).fist()
    if first_state is not None:
        print ("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")
    session.close()
