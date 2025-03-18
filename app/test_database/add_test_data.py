from app.core.database import library_engine, session
from app.models.authors import Authors
from app.models.books import Books, Genre
from app.models.clients import Clients
from app.models.orders import Orders, BorrowingStatus
from app.models.base import Base
from datetime import date, timedelta
from sqlalchemy.orm import Session



def create_table():
    Base.metadata.create_all(library_engine)
    print("database upload seccesfully")


def populate_database():
    today = date.today()
    with Session(library_engine) as session:
        # Авторы
        authors = [
            Authors(
                first_name="Федор",
                last_name="Достоевский",
                birth_date=date(1821, 11, 11),
                death_date=date(1881, 2, 9)
            ),
            Authors(
                first_name="Михаил",
                last_name="Булгаков",
                birth_date=date(1891, 5, 15),
                death_date=date(1940, 3, 10)
            ),
            Authors(
                first_name="Антон",
                last_name="Чехов",
                birth_date=date(1860, 1, 29),
                death_date=date(1904, 7, 15)
            )
        ]
        session.add_all(authors)
        session.flush()

        # Книги
        books = [
            # Достоевский
            Books(
                title="Преступление и наказание",
                year=1866,
                genre=Genre.thriller,
                rating=4.8,
                publisher="Русский вестник",
                pages=574,
                author_id=authors[0].id
            ),
            Books(
                title="Бесы",
                year=1872,
                genre=Genre.thriller,
                rating=4.7,
                publisher="Русский вестник",
                pages=768,
                author_id=authors[0].id
            ),
            Books(
                title="Идиот",
                year=1869,
                genre=Genre.thriller,
                rating=4.6,
                publisher="Русский вестник",
                pages=640,
                author_id=authors[0].id
            ),
            # Булгаков
            Books(
                title="Мастер и Маргарита",
                year=1967,
                genre=Genre.fantasy,
                rating=4.9,
                publisher="Москва",
                pages=480,
                author_id=authors[1].id
            ),
            Books(
                title="Роковые яйца",
                year=1925,
                genre=Genre.science_fiction,
                rating=4.5,
                publisher="Недра",
                pages=81,
                author_id=authors[1].id
            ),
            Books(
                title="Собачье сердце",
                year=1925,
                genre=Genre.science_fiction,
                rating=4.7,
                publisher="Художественная литература",
                pages=123,
                author_id=authors[1].id
            ),
            Books(
                title="Белая гвардия",
                year=1925,
                genre=Genre.biography,
                rating=4.6,
                publisher="Россия",
                pages=416,
                author_id=authors[1].id
            ),
            Books(
                title="Записки юного врача",
                year=1926,
                genre=Genre.autobiography,
                rating=4.5,
                publisher="Медицинский работник",
                pages=160,
                author_id=authors[1].id
            ),
            Books(
                title="Морфий",
                year=1927,
                genre=Genre.autobiography,
                rating=4.4,
                publisher="Медицинский работник",
                pages=80,
                author_id=authors[1].id
            ),
            # Чехов
            Books(
                title="Вишневый сад",
                year=1904,
                genre=Genre.romance,
                rating=4.6,
                publisher="Знание",
                pages=96,
                author_id=authors[2].id
            ),
            Books(
                title="Толстый и тонкий",
                year=1883,
                genre=Genre.romance,
                rating=4.3,
                publisher="Осколки",
                pages=32,
                author_id=authors[2].id
            )
        ]
        session.add_all(books)
        session.flush()

        # Клиенты
        clients = [
            Clients(
                first_name="Юлия",
                last_name="Перевалова",
                email="julia.p@example.com",
                phone="9001234567",
                address="ул. Ленина, 1, кв. 10"
            ),
            Clients(
                first_name="Максим",
                last_name="Гребенщиков",
                email="max.g@example.com",
                phone="9007654321",
                address="ул. Пушкина, 15, кв. 42"
            )
        ]
        session.add_all(clients)
        session.flush()

        # Заказы
        orders = [
            # Юлия Перевалова
            Orders(
                client_id=clients[0].id,
                book_id=books[3].id,  # Мастер и Маргарита
                order_date=today - timedelta(days=10),
                return_date=None,
                borrowing_status=BorrowingStatus.active
            ),
            Orders(
                client_id=clients[0].id,
                book_id=books[9].id,  # Вишневый сад
                order_date=today - timedelta(days=5),
                return_date=None,
                borrowing_status=BorrowingStatus.active
            ),
            # Максим Гребенщиков
            Orders(
                client_id=clients[1].id,
                book_id=books[5].id,  # Собачье сердце
                order_date=today - timedelta(days=15),
                return_date=None,
                borrowing_status=BorrowingStatus.active
            ),
            Orders(
                client_id=clients[1].id,
                book_id=books[2].id,  # Идиот
                order_date=today - timedelta(days=7),
                return_date=None,
                borrowing_status=BorrowingStatus.active
            ),
            Orders(
                client_id=clients[1].id,
                book_id=books[9].id,  # Вишневый сад
                order_date=today - timedelta(days=20),
                return_date=today - timedelta(days=5),
                borrowing_status=BorrowingStatus.returned
            )
        ]
        session.add_all(orders)
        session.commit()

if __name__ == "__main__":
    populate_database()

