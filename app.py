import falcon
from resources import HealthResource

app = falcon.API()
app.add_route("/health", HealthResource())


if __name__ == "__main__":
    import cheroot.wsgi
    import prometheus_client

    prometheus_client.start_http_server(9102)
    server = cheroot.wsgi.Server(("0.0.0.0", 8080), app)
    server.start()
