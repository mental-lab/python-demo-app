import os


class Config(object):
    defaultKey = os.urandom(12).hex()
    SECRET_KEY = os.environ.get('NOTES_SECRET_KEY') or defaultKey
