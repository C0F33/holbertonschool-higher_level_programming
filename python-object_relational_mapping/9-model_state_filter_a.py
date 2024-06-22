#!/usr/bin/python3
"""Module to retrieve data from the database"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    try:
        engine = create_engine( "mysql+mysqldb://{}:{}@localhost/{}".format(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3])), pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        session = Session()

        rows = session.query(State).filter(State.name.like("%a%")).all()
        for row in rows:
            print("{0}: {1}".format(row.id, row.name))
    except Exception as e:
        print("An error occurred: ", e)