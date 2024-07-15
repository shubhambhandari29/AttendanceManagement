from flask import Flask
from .auth import auth_bp
from .roster import roster_bp
from .attendance import attendance_bp

def init_routes(app: Flask):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(roster_bp, url_prefix='/roster')
    app.register_blueprint(attendance_bp, url_prefix='/attendance')
