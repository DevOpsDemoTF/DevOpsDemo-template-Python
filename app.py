import falcon
import health

app = falcon.API()
app.add_route("/health", health.Resource())


if __name__ == "__main__":
    import bjoern
    bjoern.run(app, "0.0.0.0", 8080)
