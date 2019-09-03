from prometheus_client import multiprocess, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST


def app(environ, start_response):
    """Serve Prometheus metrics"""

    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    data = generate_latest(registry)
    status = '200 OK'
    response_headers = [
        ('Content-type', CONTENT_TYPE_LATEST),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([data])


if __name__ == "__main__":
    import bjoern
    bjoern.run(app, "0.0.0.0", 9102)
