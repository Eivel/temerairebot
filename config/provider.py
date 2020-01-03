import os
from dotenv import load_dotenv

load_dotenv()

conf = {
    'BOT_TOKEN': os.getenv('BOT_TOKEN'),
    'TELEGRAM_API_ID': os.getenv('TELEGRAM_API_ID'),
    'TELEGRAM_API_HASH': os.getenv('TELEGRAM_API_HASH'),
    'TELEGRAM_API_SESSION_NAME': os.getenv('TELEGRAM_API_SESSION_NAME')
}


class Config(object):
    def __init__(self):
        self._config = conf

    def get_property(self, property_name):
        if property_name not in self._config.keys():
            raise KeyError(f'No configuration key {property_name} found')
        return self._config[property_name]


class TelegramConfig(Config):
    @property
    def bot_token(self):
        return self.get_property('BOT_TOKEN')

    @property
    def telegram_api_id(self):
        return self.get_property('TELEGRAM_API_ID')

    @property
    def telegram_api_hash(self):
        return self.get_property('TELEGRAM_API_HASH')

    @property
    def telegram_api_session_name(self):
        return self.get_property('TELEGRAM_API_SESSION_NAME')
