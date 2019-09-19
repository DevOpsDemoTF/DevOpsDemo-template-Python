import cheroot.wsgi

from config import Configuration
from routes.routing import get_app
import prometheus_client


def main():
    config = Configuration()
    init_metrics()

    config.log.info("Service has been started", extra=config.values)

    app = get_app(config)
    server = cheroot.wsgi.Server(("0.0.0.0", 8080), app)
    server.start()


def init_metrics():
    prometheus_client.start_http_server(9102)


if __name__ == "__main__":
    main()
