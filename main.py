import app.tgbot as tgbot

class Application:
    # todo
    def __init__(self, api_key, path_to_model, db_config):
        self.tgbot = tgbot.Tgbot(api_key, path_to_model, db_config)

    def run(self):
        pass

def get_config():
    # todo
    pass

if __name__ == '__main__':
    api_key, path_to_model, db_config = get_config()
    app = Application(api_key, path_to_model, db_config)
    app.run()
