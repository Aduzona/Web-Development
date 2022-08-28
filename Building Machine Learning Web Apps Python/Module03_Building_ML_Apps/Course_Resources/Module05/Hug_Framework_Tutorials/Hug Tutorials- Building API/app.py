import hug
import json


# Load Data
with open("books.json") as f:
	books_data = json.load(f)

# CLI

@hug.cli()
# API
@hug.get('/api/v1/books')
@hug.local()
def get_books():
	"""Show All Books"""
	return {"results":books_data}


@hug.get('/api/v1/books/fields')
def get_book(title:hug.types.text):
	"""Get Book By Title"""
	book = [ book for book in books_data if book["title"] == title ]
	return {"results":book}

@hug.get('/api/v1/books/lang')
@hug.local()
def get_book_by_language(language:hug.types.text):
	"""Get Book By language"""
	book = [ book for book in books_data if book["language"] == language ]
	return {"results":book}

if __name__ == '__main__':
	get_books.interface.cli()