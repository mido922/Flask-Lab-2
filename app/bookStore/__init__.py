from flask import Blueprint

bookStore_blueprint = Blueprint("bookStore",__name__,url_prefix="/books")

from app.bookStore import views