from datetime import datetime
from flask import Blueprint, Response, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from pymongo import MongoClient
from utils.decorators import staff_required, manager_required
from bson import json_util
attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/mark', methods=['POST'])
@jwt_required()
@staff_required
def mark_attendance():
    data = request.get_json()
    logged_in_user = get_jwt_identity()

    # Ensure the user can only mark attendance for themselves
    username = logged_in_user.get('username')
    if data.get('username') != username:
        return jsonify(msg="You can only mark attendance for yourself"), 403

    # Connect to MongoDB
    client = MongoClient(current_app.config['MONGO_URI'])
    db = client['attendance_db']
    users_collection = db['users']
    attendance_collection = db['attendance']

    # Check if the user exists and is a staff member
    user = users_collection.find_one({'username': username})
    if not user or user.get('role') != 'staff':
        return jsonify(msg="User does not exist or is not a staff member"), 403
    
    timestamp = datetime.now()

    # Insert attendance record
    attendance_collection.insert_one({
        'username': username,
        'date': timestamp,
        'marked': True
    })
    return jsonify({'msg': 'Attendance marked successfully'}), 201


@attendance_bp.route('/summary', methods=['GET'])
@manager_required
def attendance_summary():

    client = MongoClient(current_app.config['MONGO_URI'])
    db = client['attendance_db']
    attendance_collection = db['attendance']

    summary = list(attendance_collection.find())
    return Response(json_util.dumps(summary), mimetype='application/json')
