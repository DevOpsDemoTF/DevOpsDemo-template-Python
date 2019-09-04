import os
import logging
from pythonjsonlogger import jsonlogger
from datetime import datetime


class Configuration:
    def __init__(self):
        self._values = dict()
        self._init_logger()

    def _init_logger(self):
        self._values['DEBUG_LEVEL'] = os.getenv("DEBUG_LEVEL", "DEBUG")
        logger = logging.getLogger()

        handler = logging.StreamHandler()
        formatter = _CustomJsonFormatter('(time) (level) (msg)')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(self._values['DEBUG_LEVEL'])
        self._logger = logger

    @property
    def values(self):
        return self._values

    @property
    def logger(self):
        return self._logger


class _CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        if not log_record.get('time'):
            log_record['time'] = datetime.utcfromtimestamp(record.created).isoformat(' ')
        if log_record.get('level'):
            log_record['level'] = log_record['level'].lower()
        else:
            log_record['level'] = record.levelname.lower()

    def jsonify_log_record(self, log_record):
        return self.json_serializer(log_record, ensure_ascii=True, separators=(',', ':'), cls=jsonlogger.JsonEncoder)
