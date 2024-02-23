from flask import render_template, redirect, url_for, request, flash, current_app
from app.models import Book, db
from app.bookStore import bookStore_blueprint
import datetime
import os


def get_index():
    return "<a href='http://127.0.0.1:5000/books'> Click to go to website </a>"

@bookStore_blueprint.route("/", endpoint='bookStore_index')
def bookStore_index():
    listOfBooks = Book.get_all_objects()

    return render_template("bookStore/homepage.html",books=listOfBooks)

@bookStore_blueprint.route("/<int:id>", endpoint="bookStore_show")
def bookDetails(id):
    selectedBook = Book.query.get_or_404(id)
    return render_template("bookStore/bookDetails.html",selectedBook=selectedBook)

@bookStore_blueprint.route("/addNewBook", methods= ['GET','POST'], endpoint="create")
def create_Book():
    if request.method == 'POST':
        print(f"request recieved > {request.form}")
        file=request.files['file']
        myBook = Book(
                    name=request.form['name'],
                    bookDescription=request.form['bookDescription'],
                    numberOfPages=request.form['numberOfPages'],
                    price=request.form['price'],
                    created_at=datetime.datetime.now(),
                    image=file.filename
        )
        UPLOAD_FOLDER = "static/images/"
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        db.session.add(myBook)
        db.session.commit()
        return redirect('/books')

    return render_template("bookStore/addNewBook.html")

@bookStore_blueprint.route("/updateABook/<int:bookID>", methods=['GET','POST'], endpoint="updateABook")
def updateABook(bookID):   
    if request.method=="POST":
        myBook = Book.query.get_or_404(bookID)
        myBook.name=request.form['name']
        myBook.bookDescription=request.form['bookDescription']
        myBook.numberOfPages=request.form['numberOfPages']
        myBook.price=request.form['price']
        myBook.updated_at=datetime.datetime.now()
        db.session.commit()
        return redirect('/books')
    else:
        myBook = Book.query.get_or_404(bookID)
        return render_template('bookStore/updateABook.html', book=myBook)


@bookStore_blueprint.route("/deleteABook/<int:bookID>", endpoint="deleteABook")
def deleteABook(bookID):
    myBook = Book.query.get_or_404(bookID)
    print(myBook)
    db.session.delete(myBook)
    db.session.commit()
    return redirect('/books')