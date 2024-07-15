from flask import Blueprint, request, jsonify
from pymongo import MongoClient
from utils.decorators import manager_required

roster_bp = Blueprint('roster', __name__)

@roster_bp.route('/add', methods=['POST'])
@manager_required
def add_staff():
    data = request.get_json()
    username = data.get('username')
    working_days = data.get('working_days')
    shifts = data.get('shifts')
    weekly_offs = data.get('weekly_offs')

    client = MongoClient('mongodb://localhost:27017/attendance_db')
    db = client['attendance_db']
    roster_collection = db['roster']

    roster_collection.insert_one({
        'username': username,
        'working_days': working_days,
        'shifts': shifts,
        'weekly_offs': weekly_offs
    })
    return jsonify({'msg': 'Staff added to roster successfully'}), 201

@roster_bp.route('/view', methods=['GET'])
@manager_required
def view_roster():
    client = MongoClient('mongodb://localhost:27017/attendance_db')
    db = client['attendance_db']
    roster_collection = db['roster']

    roster = list(roster_collection.find())
    return jsonify(roster), 200

@roster_bp.route('/edit/<username>', methods=['PUT'])
@manager_required
def edit_staff(username):
    data = request.get_json()
    working_days = data.get('working_days')
    shifts = data.get('shifts')
    weekly_offs = data.get('weekly_offs')

    client = MongoClient('mongodb://localhost:27017/attendance_db')
    db = client['attendance_db']
    roster_collection = db['roster']

    roster_collection.update_one(
        {'username': username},
        {'$set': {
            'working_days': working_days,
            'shifts': shifts,
            'weekly_offs': weekly_offs
        }}
    )
    return jsonify({'msg': 'Staff details updated successfully'}), 200
