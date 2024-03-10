import json
from models import Author, Quote
from part1.db_connection import establish_connection


def load_authors(file_path):
    establish_connection()

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for author_data in data:
        author = Author(
            fullname=author_data['fullname'],
            born_date=author_data['born_date'],
            born_location=author_data['born_location'],
            description=author_data['description']
        )
        author.save()


def load_quotes(file_path):
    establish_connection()

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for quote_data in data:
        author_name = quote_data['author']
        author = Author.objects.filter(fullname=author_name).first()

        if author:
            quote = Quote(
                quote=quote_data['quote'],
                author=author,
                tags=quote_data['tags']
            )
            quote.save()
        else:
            print(f"Author '{author_name}' not found. Skipping quote.")


if __name__ == '__main__':

    authors_json_file_path = 'authors.json'
    quotes_json_file_path = 'quotes.json'

    load_authors(authors_json_file_path)
    load_quotes(quotes_json_file_path)
