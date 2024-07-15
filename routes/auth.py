from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    client = MongoClient('mongodb://localhost:27017/attendance_db')
    db = client['attendance_db']
    users_collection = db['users']

    if users_collection.find_one({'username': username}):
        return jsonify({'msg': 'User already exists'}), 400

    hashed_password = generate_password_hash(password)
    users_collection.insert_one({'username': username, 'password': hashed_password, 'role': role})
    return jsonify({'msg': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    client = MongoClient('mongodb://localhost:27017/attendance_db')
    db = client['attendance_db']
    users_collection = db['users']

    user = users_collection.find_one({'username': username})
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify({'access_token': access_token}), 200

    return jsonify({'msg': 'Invalid credentials'}), 401
