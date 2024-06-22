#!/usr/bin/python3
"""Nameless module to suck data out from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    username, password, database_name, state_name = sys.argv[1:]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost/\
        {database_name}", pool_pre_ping=True,)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        result = session.query(State).filter(State.name == state_name).first()
        if result:
            print(result.id)
        else:
            print("Not found")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        session.close()
