import prometheus_client


def init_metrics():
    prometheus_client.start_http_server(9102)
