class State:
    def __init__(self, config):
        self._config = config
        self._healthy = True

    @property
    def config(self):
        return self._config

    @property
    def healthy(self):
        return self._healthy

    @property
    def log(self):
        return self._config.log
