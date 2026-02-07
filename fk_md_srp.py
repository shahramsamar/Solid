from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self):
        pass

class FileLogger(Logger):
    @abstractmethod
    def log(self):
        pass

class DatabaseLogger(Logger):
    @abstractmethod
    def log(self):
        pass

class LoggerFactory(ABC):

    @abstractmethod
    def create_logger(self):
        pass

class FileLoggerFactory(LoggerFactory):

    def create_logger(self):
        return FileLogger()

class DatabaseLoggerFactory(LoggerFactory):

    def create_logger(self):
        return DatabaseLogger()

factory = FileLoggerFactory()
logger = factory.create_logger()
logger.log("This is a log message.")

