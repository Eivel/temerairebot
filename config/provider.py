import os
from dotenv import load_dotenv
import json

load_dotenv()

MODULE_FILEPATH = os.path.dirname(os.path.abspath(__file__))
FILES_PATH = os.path.join(MODULE_FILEPATH, 'files')

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

class ChannelTravelConfig(Config):
    @property
    def channels(self):
        return self.get_property('CHANNEL_TRAVEL_CHANNELS')

    @property
    def whitelist(self):
        return self.get_property('CHANNEL_TRAVEL_WHITELIST')

    @property
    def message(self):
        return self.get_property('CHANNEL_TRAVEL_MESSAGE')

    @classmethod
    def load_channels(cls):
        with open(os.path.join(FILES_PATH, 'channel_travel', 'channels.json')) as json_file:
            data = json.load(json_file)
            return data['channels']

    @classmethod
    def load_whitelist(cls):
        with open(os.path.join(FILES_PATH, 'channel_travel', 'whitelist.json')) as json_file:
            usernames = []
            data = json.load(json_file)
            for c in data['usernames']:
                usernames.append(c.lower())
            return usernames

    @classmethod
    def load_message(cls):
        with open(os.path.join(FILES_PATH, 'channel_travel', 'message.txt')) as text_file:
            return text_file.read()

conf = {
    'BOT_TOKEN': os.getenv('BOT_TOKEN'),
    'TELEGRAM_API_ID': os.getenv('TELEGRAM_API_ID'),
    'TELEGRAM_API_HASH': os.getenv('TELEGRAM_API_HASH'),
    'TELEGRAM_API_SESSION_NAME': os.getenv('TELEGRAM_API_SESSION_NAME'),
    'CHANNEL_TRAVEL_CHANNELS': ChannelTravelConfig.load_channels(),
    'CHANNEL_TRAVEL_WHITELIST': ChannelTravelConfig.load_whitelist(),
    'CHANNEL_TRAVEL_MESSAGE': ChannelTravelConfig.load_message()
}
