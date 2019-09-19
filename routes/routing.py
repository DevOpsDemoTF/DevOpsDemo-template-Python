import falcon

from config import Configuration
from routes.handlers import HealthHandler
from routes.state import State

__all__ = ["get_app"]


def get_app(config: Configuration):
    state = State(config)

    app = falcon.API()
    app.add_route("/health", HealthHandler(state))
    return app
