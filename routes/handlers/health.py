import falcon
import prometheus_client
from routes.state import State

__all__ = ["HealthHandler"]
HEALTH_COUNTER = prometheus_client.Counter("health_counter", "Number of times the health endpoint has been called")


class HealthHandler(object):
    def __init__(self, state: State):
        self._state = state

    def on_get(self, req, resp):
        HEALTH_COUNTER.inc(1)
        resp.status = falcon.HTTP_200 if self._state.healthy else falcon.HTTP_500
