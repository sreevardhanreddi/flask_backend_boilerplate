from flask import Blueprint

gita = Blueprint("gita", __name__)

from chapters_verses.views import *
