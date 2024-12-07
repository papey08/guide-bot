import service

class Tgbot:
    # todo
    def __init__(self, api_key, path_to_model, db_config):
        self.service = service.Service(path_to_model, db_config)
