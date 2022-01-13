from enum import Enum


class RailwayConnectionErrorType(Enum):
    EXISTS = 1
    DO_NOT_EXISTS = 2

    def __str__(self):
        if self.value == self.EXISTS.value:
            return "already exists"
        elif self.value == self.DO_NOT_EXISTS.value:
            return "doesn't exists"

        return ""


class RailwayConnectionError(Exception):
    """Exception raised for errors in the railway connection.

    Attributes:
        connection -- connection which caused error
        error_type -- what type of error
    """

    def __init__(self, connection, error_type):
        self.connection = connection
        self.error_type = error_type
        super().__init__("{} -> {} {}!".format(connection[0], connection[1], error_type))