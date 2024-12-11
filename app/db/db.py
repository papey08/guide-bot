import app.entities as entities

class Db:
    # todo
    def __init__(self, db_host, db_port, db_username, db_password, db_database_name):
        pass

    # todo
    def add_user(self, username: str):
        """
        Добавляет нового пользователя
        """
        pass

    # todo
    def add_response(self, username: str, place_id: int):
        """
        Добавляет место, предложенное пользователю, в таблицу response
        """
        pass

    def find_place(self, category: str, location: str):
        """
        Находит место с заданной категорией и локацией
        Если в данной локации нет места с данной категорией, ищем место из соседней локации (app/entities/locations.py)
        Если и в соседней локации нет места с данной категорией, ищем место из любой другой локации.
        :returns: entities.Place
        """
        pass
