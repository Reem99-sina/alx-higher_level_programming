#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create the table
    Base.metadata.create_all(engine)

    # Optionally, you can also create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add example data to the table (you can modify this part as needed)
    new_state = State(name='Example State')
    session.add(new_state)
    session.commit()

    # Close the session
    session.close()
