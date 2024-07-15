from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from datetime import datetime
from pymongo import MongoClient

attendance_bp = Blueprint('attendance', __name__)

# Initialize MongoDB client and database
client = MongoClient('mongodb://localhost:27017/attendance_db')
db = client['attendance_db']

@attendance_bp.route('/mark', methods=['POST'])
@jwt_required()
def mark_attendance():
    data = request.get_json()
    username = data.get('username')
    
    if not username:
        return jsonify({"msg": "Username is required"}), 400
    
    # Capture the current timestamp
    timestamp = datetime.now()
    
    # Create the attendance record
    attendance_record = {
        'username': username,
        'timestamp': timestamp,
    }
    
    # Insert the attendance record into the database
    db.attendance.insert_one(attendance_record)
    
    return jsonify({"msg": "Attendance marked successfully"}), 200
