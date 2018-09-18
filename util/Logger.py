import logging
from logging import handlers

from util import Config

LOG_LEVEL = {'CRITICAL': logging.CRITICAL,
             'ERROR': logging.ERROR,
             'WARNING': logging.WARNING,
             'INFO': logging.INFO,
             'DEBUG': logging.DEBUG,
             'NOTSET': logging.NOTSET}

DEFAULT_FILENAME = Config.log_getter('log_filename')
DEFAULT_LOGGER_LEVEL = LOG_LEVEL[Config.log_getter('log_logger_level')]
DEFAULT_CONSOLE_LEVEL = LOG_LEVEL[Config.log_getter('log_console_level')]
DEFAULT_FILE_LEVEL = LOG_LEVEL[Config.log_getter('log_file_level')]
DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(module)s : %(message)s'
DEFAULT_DATEFMT = '%Y-%m-%d %H:%M:%S %p'


class Logger:
    def __init__(self, full_path=DEFAULT_FILENAME, console_level=DEFAULT_CONSOLE_LEVEL, file_level=DEFAULT_FILE_LEVEL):
        self.logger = logging.getLogger(full_path)
        # 设置日志格式
        format_str = logging.Formatter(DEFAULT_FORMAT)
        # 设置日志级别
        self.logger.setLevel(DEFAULT_LOGGER_LEVEL)
        # Console输出
        self.console_logger_handler = logging.StreamHandler()
        self.console_logger_handler.setFormatter(format_str)
        self.console_logger_handler.setLevel(console_level)
        # File输出
        self.file_logger_handler = handlers.TimedRotatingFileHandler(filename=full_path, when='D', backupCount=3,
                                                                     encoding='utf-8')
        self.file_logger_handler.setFormatter(format_str)
        self.file_logger_handler.setLevel(file_level)

    def __common_output(self, level, message):
        self.logger.addHandler(self.console_logger_handler)
        self.logger.addHandler(self.file_logger_handler)
        {
            'INFO': lambda msg: self.logger.info(msg),
            'DEBUG': lambda msg: self.logger.debug(msg),
            'ERROR': lambda msg: self.logger.error(msg),
            'WARNING': lambda msg: self.logger.warning(msg),
            'CRITICAL': lambda msg: self.logger.critical(msg)
        }[level](message)
        self.logger.removeHandler(self.console_logger_handler)
        self.logger.removeHandler(self.file_logger_handler)

    def debug(self, message):
        self.__common_output('DEBUG', message)

    def info(self, message):
        self.__common_output('INFO', message)

    def warning(self, message):
        self.__common_output('WARNING', message)

    def error(self, message):
        self.__common_output('ERROR', message)

    def fault(self, message):
        self.__common_output('CRITICAL', message)
