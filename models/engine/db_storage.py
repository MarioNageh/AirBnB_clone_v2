import urllib

from sqlalchemy import create_engine
from os import getenv

from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import ExtendedBase, Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self) -> None:
        port = getenv('HBNB_MYSQL_PORT') if getenv('HBNB_MYSQL_PORT') else 3306
        password = urllib.parse.quote(getenv('HBNB_MYSQL_PWD'))
        url = f"mysql+mysqldb://{getenv('HBNB_MYSQL_USER')}" \
              f":{password}@" \
              f"{getenv('HBNB_MYSQL_HOST')}:" \
              f"{port}/" \
              f"{getenv('HBNB_MYSQL_DB')}"

        self.__engine = create_engine(url, pool_pre_ping=True)
        current_db_mode = getenv('HBNB_ENV')
        if current_db_mode == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        data_tables = []
        new_dict = {}
        if cls is not None:
            data_tables = self.__session.query(cls).all()
        else:
            for subclass in ExtendedBase.get_subclasses():
                data_tables.extend(self.__session.query(subclass).all())

        for obj in data_tables:
            key = obj.__class__.__name__ + '.' + obj.id
            new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Adds new object to current Transaction"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from current session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session_factory = \
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close session"""
        self.__session.close()
