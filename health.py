import falcon
import prometheus_client

HEALTH_COUNTER = prometheus_client.Counter("health_counter", "Number of times the health endpoint has been called")


class Resource(object):
    def on_get(self, req, resp):
        HEALTH_COUNTER.inc(1)
        resp.status = falcon.HTTP_200
