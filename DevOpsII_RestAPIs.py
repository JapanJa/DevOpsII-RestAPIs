from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "price": 10.99, "stock": 50},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "price": 8.99, "stock": 75},
    {"id": 3, "title": "1984", "author": "George Orwell", "genre": "Science Fiction", "price": 12.99, "stock": 25},
    {"id": 4, "title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "genre": "Science Fiction", "price": 9.99, "stock": 100},
    {"id": 5, "title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance", "price": 7.99, "stock": 60},
]

def get_book_by_id(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return None

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        'id': len(books) + 1,
        'title': request.form['title'],
        'author': request.form['author'],
        'genre': request.form['genre'],
        'price': request.form['price'],
        'stock': request.form['stock']
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        book['title'] = request.form.get('title', book['title'])
        book['author'] = request.form.get('author', book['author'])
        book['genre'] = request.form.get('genre', book['genre'])
        book['price'] = request.form.get('price', book['price'])
        book['stock'] = request.form.get('stock', book['stock'])
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = get_book_by_id(book_id)
    if book:
        books.remove(book)
        return jsonify({'message': 'Book deleted successfully'})
    else:
        return jsonify({'error': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
