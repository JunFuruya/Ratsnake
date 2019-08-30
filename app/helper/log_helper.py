# -*- coding: UTF-8 -*-

import logging
from app.infrastructure.log_file import LogFile


class LogHelper:
    __logger = logging.getLogger(__name__)
    __unique_instance = None

    def __init__(self):
        # TODO ログファイルの位置を config で変更できるようにする
        log_folder = './logs'
        log_file_path = log_folder + '/hideout.log'
        log_file = LogFile(log_folder, log_file_path)

        self.__logger.addHandler(log_file.get_file_handler())
        pass

    @classmethod
    def get_instance(cls):
        if not cls.__unique_instance:
            cls.__unique_instance = cls()
        return cls.__unique_instance

    def debug(self, message):
        self.__logger.setLevel(logging.DEBUG)
        self.__logger.debug(message)
        pass

    def info(self, message):
        self.__logger.setLevel(logging.INFO)
        self.__logger.info(message)
        pass

    def warn(self, message):
        self.__logger.setLevel(logging.WARN)
        self.__logger.warn(message)
        pass

    def error(self, message):
        self.__logger.setLevel(logging.ERROR)
        self.__logger.error(message)
        pass

    def critical(self, message):
        self.__logger.setLevel(logging.CRITICAL)
        self.__logger.critical(message)
        pass
