#!/usr/bin/python3
"""comment this is a string"""

import sys
from model_state import State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State)

    if query.count() == 0:
        print("Nothing")
    else:
        row = query.limit(1).one()
        print("{0}: {1}".format(row.id, row.name))
