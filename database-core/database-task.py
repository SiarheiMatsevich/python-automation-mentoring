from typing import List, Type
from sqlalchemy import create_engine, Column, String, Integer, update, delete, exc
from sqlalchemy.orm import registry
from sqlalchemy.orm import sessionmaker
import argparse
import sys

DATABASE_NAME = 'films_db.db'
TABLE_NAME = 'films'

mapper_registry = registry()
Base = mapper_registry.generate_base()
engine = create_engine(f'sqlite+pysqlite:///{DATABASE_NAME}', echo=True)
Session = sessionmaker(bind=engine)


class Film (Base):
    __tablename__ = TABLE_NAME

    id = Column('id', Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column('title', String)
    director = Column('director', String)
    release_year = Column('release_year', Integer)

    def __repr__(self):
        return f'{self.id} {self.title} {self.director} {self.release_year}'


def input_films(qty: int, film_id=False) -> List[Film]:
    """
    Gets user input for 'qty' iterations and returns list of Film instances.
    """
    films = []
    for n in range(qty):
        print(f'Please enter film data({n+1})')
        film = Film(
            id=int(input('id: ')) if film_id else None,
            title=input('title: '),
            director=input('director: '),
            release_year=int(input('release_year: '))
        )
        films.append(film)
    return films


def create_table() -> None:
    """
    Creates table using global engine and meta_data
    """
    Base.metadata.create_all(bind=engine)


def add_films(*films: Film) -> None:
    """
    Adds films to the 'films' table
    """
    with Session.begin() as session:
        session.add_all(films)


def get_all_films() -> List[Type[Film]]:
    """
    Returns all existing films
    """
    with Session() as session:
        return session.query(Film).all()


def update_film(film: Film) -> None:
    """
    Finds existing film by 'id' and update it with given film data.
    Raises Attribute error if film with given id does not exist.
    """
    with Session() as session:
        film_exists = session.query(Film).where(Film.id == film.id).count() == 1

    if film_exists:
        with Session.begin() as session:
            session.execute(
                update(Film).where(Film.id == film.id).values(
                    title=film.title,
                    director=film.director,
                    release_year=film.release_year
                )
            )
    else:
        raise AttributeError(f'Film with given id does not exists in \'{TABLE_NAME}\' table ')


def delete_all_films() -> None:
    """
    Deletes all the films from 'films' table. Does not drop table
    """
    with Session.begin() as session:
        session.execute(
            delete(Film)
        )


def demo() -> None:
    """
    Demonstration of script possibilities:
    1. Creates table
    2. Adds three pre-defined films to the 'films' table
    3. Updates the second film with new pre-defined data
    4. Prints all existing films
    5. Deletes all the films from 'films' table
    """
    create_table()
    f1 = Film(title='First Film', director='Jon Doe', release_year=1999)
    f2 = Film(title='Second Film', director='Jane Doe', release_year=2003)
    f3 = Film(title='Third Film', director='John Smith', release_year=2007)
    updated_film = Film(id=2, title='Updated Film', director='Updated Director', release_year=2099)
    add_films(f1, f2, f3)
    update_film(updated_film)
    print(*get_all_films(), sep='\n')
    delete_all_films()


def parse_cmd_args():
    help_msg = 'Script for interaction with database. Run without arguments to see demo.'
    create_films_table_help = (f'Creates database with  \'{DATABASE_NAME}\' '
                               f'if does not exist and \'{TABLE_NAME}\' table with predefined columns')
    add3_help = f'Adds 3 films to the \'{TABLE_NAME}\' table'
    update_help = f'Updates existing film if exists, otherwise throws exception'
    print_help = f'Prints all data from \'{TABLE_NAME}\''
    delete_help = f'Deletes all data from \'{TABLE_NAME}\'. Does not drop table'

    parser = argparse.ArgumentParser(description=help_msg)
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--create_films_table', action='store_true', help=create_films_table_help)
    group.add_argument('--add3', action='store_true', help=add3_help)
    group.add_argument('--update', action='store_true', help=update_help)
    group.add_argument('--print', action='store_true', help=print_help)
    group.add_argument('--delete', action='store_true', help=delete_help)

    if len(sys.argv) == 1:
        demo()
        sys.exit(0)
    else:
        arg, unknown_args = parser.parse_known_args()
        if unknown_args:
            raise Exception('Unknown arg(s). Use --help to see usage')
    return arg


if __name__ == '__main__':
    flow = parse_cmd_args()
    if flow.create_films_table:
        create_table()
    elif flow.add3:
        add_films(*input_films(3))
    elif flow.update:
        update_film(*input_films(1, film_id=True))
    elif flow.print:
        res = get_all_films()
        print(*res, sep='\n')
    else:
        delete_all_films()
