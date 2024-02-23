#!/usr/bin/env python3

from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Traveler, Island

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

@app.get('/')
def index():
    return "Welcome to the API, available resources include /travelers and /islands"

# --- TRAVELER ROUTES --- #

# GET - INDEX (ALL)
@app.get('/travelers')
def travelers():
    travelers = Traveler.query.all()
    return [ travelers.to_dict() for travelers in travelers ], 200
    
# GET - FIND BY ID (SHOW)
@app.get('/traveler/<int:id>')
def get_traveler_by_(id):
    found_traveler = Traveler.query.where(Traveler.id == id).first()
    if found_traveler:
        return make_response (jsonify(found_traveler.to_dict()), 200)
    else:
        return { "error": "Not Found"}

# POST - CREATE
@app.post('/traveler')
def create_traveler():
    data= request.json

    try:
        new_traveler = Traveler(name=data.get("name"), age=data.get("age"), budget=data.get("budget"), frequent_flyer=data.get("frequent_flyer"))
        db.session.add(new_traveler)
        db.session.commit()
        return new_traveler.to_dict(), 201

    except:
        return { "error": "Invalid travler please try again"}, 405
# PATCH - UPDATE
    
@app.patch('/traveler/<int:id>')
def update_traveler(id):
    data = request.json
    found_traveler = Traveler.query.where(Traveler.id ==id).first()

    if found_traveler:
        for key in data:
            setattr( found_traveler, key, data[key] )

        db.session.commit()
        return found_traveler.to_dict(), 202
    else:
        return {"error": "Not Found"}, 404

# DELETE - DESTROY BY ID
@app.delete('/traveler/<int:db>')
def delete_traveler(id):
    found_traveler = Traveler.query.where(Traveler.id == id).first()

    if found_traveler:

        db.session.delete(found_traveler)
        db.session.commit()

        return{}, 204

    else:
        return { "error": "Not Found"}, 404
# --- ISLAND ROUTES --- #

# GET - INDEX (ALL)
@app.get('/islands')
def islands():
    islands = Island.query.all()
    return [ islands.to_dict() for islands in islands ], 200
    pass

# GET - FIND BY ID (SHOW)
@app.get('/islands/<int:id>')
def get_island_by_id(id):
    found_island = Island.query.where(Island.id == id).first()
    if found_island:
        return make_response (jsonify(found_island.to_dict()), 200)
    else:
        return {"error": "Not Found"}
# POST - CREATE
@app.post('/islands')
def create_islands():
    data = request.json

    try:

        new_islands = Island(name=data.get('name'), square_miles=data.get('square_miles'), average_temperature=data.get('averagee_temperature'))
        return new_islands.to_dict(), 201
    
    except:
        return { 'error': "Invalid island pleas try again"}, 405

# PATCH - UPDATE
@app.patch('islands/int:id>')
def update_islands(id):
    data = request.json
    found_island = Island.query.where(Island.id == id).first()

    if found_island:

        for key in data:
            setattr(found_island, key, data[key])
        
        db.session.commit()
        return found_island.to_dict(), 202
    else:
        return {"error": "Not Found"}, 404


# DELETE - DESTROY BY ID

if __name__ == '__main__':
    app.run(port=5555, debug=True)
