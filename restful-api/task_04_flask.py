#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


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
    for user in users:
        if user == username:
            return jsonify(users[user])
    return jsonify({"Error user not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data or "name" not in data:
        if "age" not in data or "city" not in data:
            return jsonify({"Error: field missing"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"Error: user already exist"}), 400

    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
        }

    return jsonify({"message": "User added successfully", username:
                    users[username]}), 201


if __name__ == "__main__":
    app.run()
