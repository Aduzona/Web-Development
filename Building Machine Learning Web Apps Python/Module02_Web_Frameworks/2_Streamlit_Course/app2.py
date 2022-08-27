import hug

# local pkg
@hug.get()
@hug.local()
def get_books(title:hug.types.text):
    """ Get Books By Title"""
    return{"title":title.upper()}

# API
#@hug.get()

# CLI
#@hug.cli()