"""
Initialize a Flask web server to serve endpoints for the GHGA project.
"""
import os

from flask import Flask


def create_app(test_config=None) -> Flask:
    """
    Create the main Flask application.
    Parameters
    ----------
    :param test_config: an instance of the Python config object

    Returns
    -------
    :return app: an instance of the Flask object
    """
    app = Flask("front-end-web-server", instance_relative_config=True)

    if test_config is None:
        # Get path to configuration file and load that configuration into Flask's app.config object.
        curr_dir = os.path.abspath(os.path.dirname(__file__))
        config_dir = os.path.dirname(curr_dir)
        config_filename = os.path.join(config_dir, "config.py")

        # load the instance config, if it exists, when not testing
        app.config.from_pyfile(config_filename)

        print(app.config.get("SECRET_KEY"))
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
    def index():
        return "Index page!"

    from .views import hello

    app.register_blueprint(hello)

    return app
