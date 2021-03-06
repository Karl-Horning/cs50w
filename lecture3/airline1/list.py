# RUN IN TERMINAL: export DATABASE_URL="postgres://karl_horning:cs50w@localhost/lecture3"
# OR, IN PLACE OF ENGINE, USE engine = create_engine('postgres://karl_horning:cs50w@localhost/lecture3')
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute('SELECT origin, destination, duration FROM flights').fetchall()
    for flight in flights:
        print(f'{flight.origin} to {flight.destination}, {flight.duration} minutes.')

if __name__ == '__main__':
    main()