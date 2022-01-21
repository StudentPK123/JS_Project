from enum import Enum

class RailwayConnectionErrorType(Enum):
    """Klasa pozwalająca na przekazanie jako parametr odpowiedniego argumentu (1 - istnieje, 2 - nie istnieje) określającego stan połączenia kolejowego"""

    EXISTS = 1
    DO_NOT_EXISTS = 2

    def __str__(self):
        if self.value == self.EXISTS.value:
            return "już istnieje"
        elif self.value == self.DO_NOT_EXISTS.value:
            return "nie istnieje"

        return ""


class RailwayConnectionError(Exception):
    """Klasa błędu wywoływana w przypadku błędów w połączeniu kolejowym.

        connection -- połączenie, które spowodowało błąd
        error_type -- jaki typ błędu
    """

    def __init__(self, connection, error_type):
        self.connection = connection
        self.error_type = error_type
        super().__init__("{} -> {} {}!".format(connection[0], connection[1], error_type))