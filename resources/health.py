import falcon
import prometheus_client
from config import Configuration

__all__ = ["HealthResource"]
HEALTH_COUNTER = prometheus_client.Counter("health_counter", "Number of times the health endpoint has been called")


class HealthResource(object):
    def __init__(self, config : Configuration):
        pass

    def on_get(self, req, resp):
        HEALTH_COUNTER.inc(1)
        resp.status = falcon.HTTP_200
