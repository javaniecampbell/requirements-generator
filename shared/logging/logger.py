from abc import ABC, abstractmethod
import enum


class LogLevel(enum.Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5


class Logger(ABC):
    @abstractmethod
    def log(
        self,
        log_levl: LogLevel,
        message: str,
        data: dict = None,
        exception: Exception = None,
    ):
        pass

    @abstractmethod
    def error(self, message: str, exception: Exception = None):
        pass

    @abstractmethod
    def warning(self, message: str):
        pass

    @abstractmethod
    def info(self, message: str, data: dict = None):
        pass

    @abstractmethod
    def debug(self, message: str, data: dict = None):
        pass

    @abstractmethod
    def critical(self, message: str, exception: Exception = None):
        pass
