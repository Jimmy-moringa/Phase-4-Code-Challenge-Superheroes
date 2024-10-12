from flask import jsonify
from app import app, db
from models import Hero, Power

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes])

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{"id": power.id, "name": power.name, "description": power.description} for power in powers])
