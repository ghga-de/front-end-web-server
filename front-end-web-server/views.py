"""
Routes for the front-end webserver.

These routes are set up using the Blueprints pattern. This Flask application uses the application
factory pattern, which means that you cannot use the app object at import time, but you can use it within a request,
once the application is running. To do this, use the current_app object that you can import from flask as documented
here: https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/."""
import pika
from flask import Blueprint, current_app

TASK_MQ_BROKER = "redis://task-mq:6379/0"  # change to Docker configuration
TASK_MQ_BACKEND = "redis://task-mq:6379/0"

hello = Blueprint("hello", __name__, url_prefix="/hello")


@hello.route("/", methods=["GET"])
def hello_world():
    """Request a run from the Hello World service."""
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=current_app.config["EVENT_MQ_BROKER"])
    )
    channel = connection.channel()
    print("Connected!")
    channel.exchange_declare(exchange="test", exchange_type="topic")

    routing_key = "test.hello.world"

    message = b"Hello World Test"
    channel.basic_publish(
        exchange="test",
        routing_key=routing_key,
        body=b"Hello World Test"
    )
    print(" [x] Sent %r:%r " % (routing_key, message), flush=True)
    connection.close()

    return "Hello World task requested."
