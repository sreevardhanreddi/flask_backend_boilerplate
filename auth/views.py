from flask import jsonify, request
from auth import auth


@auth.route("/login/", methods=["POST",])
def user_login():
    """ accepts user credentials and returns auth token."""
    return jsonify({"token": "token"}), 200


@auth.route("/register/", methods=["GET", "POST",])
def user_registration():
    """ registers a user and returns auth token """
    return jsonify({"token": "token"}), 200

