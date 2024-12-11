import neuro
import db

class Service:
    # todos
    def __init__(self, path_to_model, db_config):
        self.neuro = neuro.Neuro(path_to_model)
        self.db = db.Db(db_config)

    # todo
    def add_user(self, username: str):
        """
        добавить пользователя в БД по нику в тг
        """
        pass

    def find_place(self, username: str, area, duration, budget, time, type_l, location):
        """
        :params:
            username: ник в тг
            area: улица - 1, помещение - 2
            duration: 1 час = 1, 3 часа = 3, 6 часов = 6
            budget: до 1000 рублей = 1000, больше 1000 = 10000
            time: утро = 1, день = 2, вечер = 3, ночь = 4
            type_l: активный = 1, пассивный = 2
            location: трехбуквенное обозначение округа (ЦАО, САО и тд)
        :returns:
            place: entities.Place
        """
        pass
