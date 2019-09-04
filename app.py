import cheroot.wsgi
import falcon

from config import Configuration
from metrics import init_metrics
from resources import HealthResource


def get_api(config: Configuration):
    app = falcon.API()
    app.add_route("/health", HealthResource(config))
    return app


def main():
    config = Configuration()
    init_metrics()

    config.logger.info("Service starting", extra=config.values)

    app = get_api(config)
    server = cheroot.wsgi.Server(("0.0.0.0", 8080), app)
    server.start()


if __name__ == "__main__":
    main()
