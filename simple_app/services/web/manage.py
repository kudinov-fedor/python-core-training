from flask.cli import FlaskGroup

from project import app, db, User, Book, Author


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    user_1 = User(email="fkudi@gmail.com")

    author = Author("Joan", "Roaling")
    books = [
        Book("Harry 1", author),
        Book("Harry 2", author),
        Book("Harry 3", author),
    ]
    user_2 = User(email="michael@mherman.org", books=books[:2])

    db.session.add(user_1)
    db.session.add(user_2)
    db.session.commit()


if __name__ == "__main__":
    cli()
