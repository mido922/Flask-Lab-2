from flask import render_template
from app.models import Book




def students_index():
    listOfBooks = Book.get_all_objects()

    return render_template("bookStore/index.html",books=listOfBooks)