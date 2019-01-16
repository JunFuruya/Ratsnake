# -*- coding: UTF-8 -*-

import logging

class LogHelper():
    __logger = logging.getLogger(__name__)
    __file_handler = None
    
    def __init__(self):
        if self.__file_handler is None:
            # TODO ログファイルの位置を config で変更できるようにする
            self.__file_handler = logging.FileHandler('./logs/hideout.log')
            self.__file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)8s %(message)s"))
            self.__logger.addHandler(self.__file_handler)
        pass

    def debug(self, message):
        self.__logger.setLevel(logging.DEBUG)
        self.__logger.debug(message)
        pass
    
    def info(self, message):
        self.__logger.setLevel(logging.INFO)
        self.__logger.debug(message)
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
 