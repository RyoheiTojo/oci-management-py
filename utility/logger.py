from abc import ABCMeta, abstractmethod
from typing import Dict
from enum import IntEnum, auto

class LogLevel(IntEnum):
    UNKNOWN = auto()
    DEBUG   = auto()
    INFO    = auto()
    WARN    = auto()
    ERROR   = auto()

    @classmethod
    def of_string(cls, level:str):
        if level == "DEBUG":
            return cls.DEBUG
        elif level == "INFO":
            return cls.INFO
        elif level == "WARN":
            return cls.WARN
        elif level == "ERROR":
            return cls.ERROR
        else:
            return cls.UNKNOWN

class Logger(metaclass=ABCMeta):
    @abstractmethod
    def debug(self, json:Dict):
        raise NotImplementedError

    @abstractmethod
    def info(self, json:Dict):
        raise NotImplementedError

    @abstractmethod
    def warn(self, json:Dict):
        raise NotImplementedError

    @abstractmethod
    def error(self, json:Dict):
        raise NotImplementedError

def getLogger(level:LogLevel):
    return LoggingLogger(level = level)

import logging
import datetime
from pythonjsonlogger import jsonlogger
from pytz import timezone

class LoggingLogger(Logger):
    logger: logging.Logger

    def __init__(self, level:LogLevel, path:str, fmt:str):
        logging_level = logging.DEBUG
        if level == LogLevel.DEBUG:
            logging_level = logging.DEBUG
        elif level == LogLevel.INFO:
            logging_level = logging.INFO
        elif level == LogLevel.WARN:
            logging_level = logging.WARN
        elif level == LogLevel.ERROR:
            logging_level = logging.ERROR

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging_level)

        sh = logging.StreamHandler()
        sh.setLevel(logging_level)
        sh.setFormatter(JsonFormatter())
        self.logger.addHandler(sh)
        del sh

        fh = logging.FileHandler(path, mode='a', encoding='utf-8')
        fh.setLevel(logging_level)
        fh.setFormatter(JsonFormatter())
        self.logger.addHandler(fh)
        del fh

    def debug(self, json:Dict):
        self.logger.debug(json)

    def info(self, json:Dict):
        self.logger.info(json)

    def warn(self, json:Dict):
        self.logger.warn(json)

    def error(self, json:Dict):
        self.logger.error(json)

class JsonFormatter(jsonlogger.JsonFormatter):

    def parse(self):
        return [
            'process',
            'timestamp',
            'level',
            'name',
            'message',
            'stack_info',
        ]

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # https://qiita.com/yoppe/items/4260cf4ddde69287a632
            now = datetime.datetime.now(timezone('Asia/Tokyo')).strftime('%Y-%m-%dT%H:%M:%S%z')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

