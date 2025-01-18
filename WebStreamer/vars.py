# (c) @EverythingSuckz | @AbirHasan2005

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID', '25334837'))
    API_HASH = str(getenv('API_HASH', '3432471e77ec691aa812618c4c93d68b'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '7576907173:AAGwZsRL4NdjJn63AZAtn16q7j-Z9EbkIUE'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'AHFile2LinkBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL, '-1002423883508'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(getenv('OWNER_ID', '7711280170'))
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU else APP_NAME+'.herokuapp.com'
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://titu:titu@titu.cfdnr.mongodb.net/?retryWrites=true&w=majority&appName=titu'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
