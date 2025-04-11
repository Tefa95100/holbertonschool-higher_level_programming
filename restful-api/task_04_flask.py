#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/status")
def get_status():
    return "OK"


@app.route("/data", methods=['GET'])
def get_users():
    return jsonify(list(users.keys()))


@app.route("/users/<string:username>", methods=["GET"])
def get_username(username):
    if username in users:
        user = users[username].copy()
        user["username"] = username
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    if "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    if "age" not in data:
        return jsonify({"error": "Age is required"}), 400
    if "city" not in data:
        return jsonify({"error": "City is required"}), 400

    username = data["username"]

    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
        }

    return jsonify({
        "message": "User added",
        "user": {
            "username": username,
            "name": data["name"],
            "age": data["age"],
            "city": data["city"]
        }
    }), 201


if __name__ == "__main__":
    app.run()
