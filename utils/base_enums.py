from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.value, i.name.title()) for i in cls)
