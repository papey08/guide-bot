import psycopg2
from app.entities.locations import locations
from app.entities.place import Place
from user_query import UserQuery


class Db:
    def __init__(self, db_host, db_port, db_username, db_password, db_database_name):
        self.connection = psycopg2.connect(
            host=db_host,
            port=db_port,
            user=db_username,
            password=db_password,
            dbname=db_database_name
        )
        self.connection.autocommit = True

    def add_user(self, username: str):
        with self.connection.cursor() as cursor:
            cursor.execute(UserQuery.ADD_USER, (username,))

    def add_response(self, username: str, place_id: int):
        with self.connection.cursor() as cursor:
            cursor.execute(UserQuery.ADD_RESPONSE, (place_id, username))

    def execute_find_place(self, query: str, vars: tuple):
        with self.connection.cursor() as cursor:
            cursor.execute(query, vars)
            row = cursor.fetchone()
            if row:
                return Place(
                    name=row[1],
                    url=row[2],
                    location=row[3]
                )

    def find_place(self, category: str, location: str):
        place = self.execute_find_place(UserQuery.FIND_PLACE_BY_CATEGORY_AND_LOCATION, (category, location));
        if place:
            return place
        neighbors = locations.get(location, [])
        for neighbor in neighbors:
            place = self.execute_find_place(UserQuery.FIND_PLACE_BY_CATEGORY_AND_LOCATION, (neighbor, location));
            if place:
                return place
        place = self.execute_find_place(UserQuery.FIND_PLACE_BY_CATEGORY, (category,));
        if place:
            return place
        return Place()
