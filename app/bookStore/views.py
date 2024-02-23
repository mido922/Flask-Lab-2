from flask import render_template
from app.models import Book
from app.bookStore import bookStore_blueprint


def get_index():
    return "<h1> Test???<h1>"

@bookStore_blueprint.route("/", endpoint='bookStore_index')
def bookStore_index():
    listOfBooks = Book.get_all_objects()

    return render_template("bookStore/index.html",books=listOfBooks)