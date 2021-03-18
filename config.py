"""Flask configuration"""
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
secrets_file = os.path.join(basedir, ".env")
load_dotenv(secrets_file)

TESTING = True
DEBUG = True
FLASK_ENV = "development"
SECRET_KEY = os.environ.get(
    "SECRET_KEY"
)  # Configure secrets from environment to prevent any chance of publication

EVENT_MQ_BROKER = "event-mq"
EVENT_MQ_USER = "guest"
EVENT_MQ_PASSWORD = "guest"
EVENT_MQ_PORT = 5672
EVENT_MQ_VHOST = "/"
EVENT_MQ_URL = f"amqp://{EVENT_MQ_USER}:{EVENT_MQ_PASSWORD}@{EVENT_MQ_BROKER}:{EVENT_MQ_PORT}/{EVENT_MQ_VHOST}"
