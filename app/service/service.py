import neuro
import db

class Service:
    # todos
    def __init__(self, path_to_model, db_config):
        self.neuro = neuro.Neuro(path_to_model)
        self.db = db.Db(db_config)
