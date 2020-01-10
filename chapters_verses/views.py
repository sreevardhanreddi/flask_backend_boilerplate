from flask import jsonify, request
from chapters_verses import gita


@gita.route("/chapters/", methods=["GET",])
def chapters():
    """ returns list of chapters."""
    return jsonify({"chapters": "chapters"}), 200


@gita.route("/<int:chapter_id>/verses/", methods=["GET",])
def verses(chapter_id):
    """ returns list of verses in a chapter."""
    return jsonify({"verses": "chapter {} verses".format(chapter_id)}), 200

