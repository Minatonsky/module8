from models import Author, Quote
from db_connection import establish_connection


def search_quotes(query):
    tags = query.split(',')
    quotes = Quote.objects.filter(tags__all=tags)

    return quotes


if __name__ == '__main__':
    establish_connection()

    while True:
        command = input("Введіть команду: ")

        if command.startswith('name:'):
            author_name = command.split(':')[1].strip()
            author = Author.objects.filter(fullname=author_name).first()

            if author:
                quotes = Quote.objects.filter(author=author)
                for quote in quotes:
                    print(quote.quote)
            else:
                print(f"Автор з ім'ям '{author_name}' не знайдений.")

        elif command.startswith('tag:'):
            tag = command.split(':')[1].strip()
            quotes = search_quotes(tag)
            for quote in quotes:
                print(quote.quote)

        elif command.startswith('tags:'):
            tags = command.split(':')[1].strip()
            quotes = search_quotes(tags)
            for quote in quotes:
                print(quote.quote)

        elif command == 'exit':
            break

        else:
            print("Невідома команда. Спробуйте ще раз.")
