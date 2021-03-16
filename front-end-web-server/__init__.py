import os

from flask import Flask


# Here are some global configuration variables. They MUST offloaded into standard Python configuration. Having them
# here is simply convenience and to avoid adding complexity by switching to setup.cfg or equivalent.

# The Message Queue (RabbitMQ) that mediates events between microservices
EVENT_MQ_BROKER = "event-mq"
EVENT_MQ_USER = "guest"
EVENT_MQ_PASSWORD = "guest"
EVENT_MQ_PORT = 5672
EVENT_MQ_VHOST = "event-host"
EVENT_MQ_URL = f"amqp://{EVENT_MQ_USER}:{EVENT_MQ_PASSWORD}@{EVENT_MQ_BROKER}:{EVENT_MQ_PORT}//"  # {EVENT_MQ_VHOST}"


def create_app(test_config=None):
    app = Flask("front-end-web-server", instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        EVENT_MQ_BROKER=EVENT_MQ_BROKER
        # DATABASE=
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hell
    @app.route("/")
    def hello():
        return "Index page!"

    from .views import hello
    app.register_blueprint(hello)

    return app
