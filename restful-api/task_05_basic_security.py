#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_jwt_extended import get_jwt_identity, get_jwt, exceptions
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

app.config["JWT_SECRET_KEY"] = "cle_secrete"

jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        return username


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


@auth.error_handler
def error_auth():
    return jsonify({"message": "User or password incorrect"}), 401


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        access_token = create_access_token(identity=username,
                                           additional_claims={"role": users[
                                               username]["role"]})
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    try:
        current_user = get_jwt_identity()
        if not current_user:
            return jsonify({"error": "Invalid token"}), 401
        return jsonify({"message": "JWT Auth: Access Granted",
                        "user": current_user}), 200
    except exceptions.NoAuthorizationError:
        return jsonify({"error": "Missing or invalid token"}), 401


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    token_received = get_jwt()
    if token_received.get("role") == "admin":
        return jsonify({"message": "Admin Access: Granted"}), 200
    return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
