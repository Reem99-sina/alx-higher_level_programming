#!/usr/bin/python3
"""Script that deletes a State object from the database hbtn_0e_6_usa"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Get the State with the specified id
    state_id_to_delete = 6  # Replace with the id you want to delete
    state_to_delete = session.query(State).filter_by(id=state_id_to_delete).first()

    if state_to_delete:
        # Delete the State from the session
        session.delete(state_to_delete)

        # Commit the changes to the database
        session.commit()
        print(f"State with id {state_id_to_delete} deleted successfully.")
    else:
        print(f"No State found with id {state_id_to_delete}.")

    # Close the session
    session.close()
