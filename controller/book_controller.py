from flask import render_template,Blueprint,request,redirect
from models.book_list import book_list, Book

book_blueprint = Blueprint("book_list", __name__)

@book_blueprint.route('/')
def index():
    return render_template("index.jinja", title = "Library Home", book_list=book_list)

@book_blueprint.route('/books')
def list_of_books():
    return render_template("books.jinja", title = "List of Books", book_list=book_list)

@book_blueprint.route('/books/<title>')
def inidividual_book(title):
    found_book = None
    for book in book_list:
        if book.title == title:
            found_book = book
    print(found_book)        
    return render_template("book.jinja", title = title, book = found_book)


@book_blueprint.route('/books', methods = ["POST"])
def add_book_to_list():
    title = request.form["title"]
    author = request.form["author"]
    genre = request.form["genre"]
    new_book = Book(title, author, genre)
    book_list.append(new_book)
    return redirect('/books')

@book_blueprint.route('/books/delete/<title>', methods = ["POST"])
def remove_from_list(title):
    found_book = None
    for book in book_list:
        if book.title == title:
            found_book = book
    book_list.remove(found_book)
    return redirect('/books')


