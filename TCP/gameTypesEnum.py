import enum


class GameTypesEnum(enum.IntEnum):
    DotsAndCrosses = 1
    GuessingGame = 2


class NoSuchGame(Exception):
    def __init__(self, message):
        super(NoSuchGame, self).__init__(message)

