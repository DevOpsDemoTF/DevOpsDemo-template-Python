FROM alpine:3.10 as build
RUN apk add --no-cache \
    python3 \
    python3-dev \
    py3-pip

RUN python3 -m venv --copies /app/venv
WORKDIR /app

COPY . /app/
RUN /app/venv/bin/pip install -r dependencies.txt

FROM alpine:3.10 as test
RUN apk add --no-cache \
      python3

COPY --from=build /app /app
WORKDIR /app

RUN /app/venv/bin/pip install nose
RUN /app/venv/bin/nosetests --with-xunit --xunit-file /app/test-results.xml tests/

FROM alpine:3.10
RUN mkdir /app && \
    addgroup -S app && adduser -S app -G app && \
    apk add --no-cache \
      python3

EXPOSE 8080
EXPOSE 9102

ENV DEBUG_LEVEL DEBUG

COPY --from=build /app /app
COPY --from=test /app/test-results.xml /app/

USER app
WORKDIR /app
CMD ["/app/venv/bin/python", "app.py"]
