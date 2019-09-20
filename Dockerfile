FROM alpine:3.10 as build
RUN apk add --no-cache \
    python3 \
    python3-dev \
    py3-pip

RUN python3 -m venv --copies /app/venv
WORKDIR /app

COPY . /app/
RUN /app/venv/bin/pip install -r dependencies.txt

FROM build as test

RUN /app/venv/bin/pip install nose
RUN /app/venv/bin/nosetests --with-xunit --xunit-file /app/test-results.xml tests/

FROM alpine:3.10
RUN addgroup -S app && adduser -S app -G app && \
    apk add --no-cache \
    python3 \
    dumb-init

EXPOSE 8080
EXPOSE 9102

ENV DEBUG_LEVEL DEBUG

COPY --from=build /app /app
COPY --from=test /app/test-results.xml /app/

USER app
WORKDIR /app
ENTRYPOINT ["dumb-init", "/app/venv/bin/python"]
CMD ["app.py"]
