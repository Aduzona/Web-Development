import hug


# Local Pkg
# API
# CLI

@hug.cli()
@hug.get('/books')
@hug.local()
def get_books(title:hug.types.text):
	"""Get Books By Title"""
	return {"title":title.upper()}



# For CLI
if __name__ == '__main__':
	get_books.interface.cli()
