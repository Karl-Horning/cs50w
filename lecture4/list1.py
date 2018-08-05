# RUN IN TERMINAL: export DATABASE_URL="postgres://karl_horning:cs50w@localhost/lecture4"
# OR, IN PLACE OF ENGINE, USE engine = create_engine('postgres://karl_horning:cs50w@localhost/lecture4')
import os


from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def main():
    flights = Flight.query.all()
    for flight in flights:
        print(f'{flight.origin} to {flight.destination}, {flight.duration} minutes.')

if __name__ == '__main__':
    with app.app_context():
        main()
