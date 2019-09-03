FROM alpine:3.10 as build
RUN apk add --no-cache \
    libev-dev \
    python3 \
    python3-dev \
    py3-pip \
    py3-nose

RUN python3 -m venv --copies /app/venv
WORKDIR /app

COPY dependencies.txt supervisord.conf .
RUN /app/venv/bin/pip install dependencies.txt
RUN nosetests --with-xunit --xunit-file test-results.xml tests/

FROM alpine:3.10
RUN mkdir /app && \
    addgroup -S app && adduser -S app -G app && \
    apk add --no-cache
        supervisor \
        libev \
        useradd

EXPOSE 8080
EXPOSE 9102

ENV DEBUG_LEVEL DEBUG
ENV prometheus_multiproc_dir /app/.metrics

VOLUME /app/.metrics

COPY --from=build /app /app
USER app
WORKDIR /app
CMD ["/usr/bin/supervisord", "-c", "/app/supervisord.conf"]