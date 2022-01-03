from abc import ABCMeta, abstractmethod
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
    def debug(self, message:str):
        raise NotImplementedError

    @abstractmethod
    def info(self, message:str):
        raise NotImplementedError

    @abstractmethod
    def warn(self, message:str):
        raise NotImplementedError

    @abstractmethod
    def error(self, message:str):
        raise NotImplementedError

import logging
import datetime
from pythonjsonlogger import jsonlogger
from pytz import timezone

def setLogger(name:str, level:LogLevel, path:str):
    logging_level = logging.ERROR

    if level == LogLevel.DEBUG:
        logging_level = logging.DEBUG
    elif level == LogLevel.INFO:
        logging_level = logging.INFO
    elif level == LogLevel.WARN:
        logging_level = logging.WARN
    elif level == LogLevel.ERROR:
        logging_level = logging.ERROR

    logger = logging.getLogger(name)
    logger.setLevel(logging_level)

    sh = logging.StreamHandler()
    sh.setLevel(logging_level)
    sh.setFormatter(JsonFormatter())
    logger.addHandler(sh)
    del sh

    fh = logging.FileHandler(path, mode='a', encoding='utf-8')
    fh.setLevel(logging_level)
    fh.setFormatter(JsonFormatter())
    logger.addHandler(fh)
    del fh
  
def getLogger(name:str):
    return LoggingLogger(logger = logging.getLogger(name))

class LoggingLogger(Logger):
    logger: logging.Logger

    def __init__(self, logger:logging.Logger):
        self.logger = logger

    def debug(self, message:str):
        self.logger.debug(message)

    def info(self, message:str):
        self.logger.info(message)

    def warn(self, message:str):
        self.logger.warn(message)

    def error(self, message:str):
        self.logger.error(message)

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

