from enum import Enum


class OwnerGender(Enum):
    MALE = 'M'
    FEMALE = 'F'


class RealEstateType(Enum):
    REAL_ESTATE = 'B'
    FLAT = 'F'
    ROOM = 'R'


class FlatType(Enum):
    REGULAR = 'R'
    STUDIO = 'S'


class RoomType(Enum):
    BATHROOM = 'B'
    KITCHEN = 'K'
    LIVING_ROOM = 'L'


class PriceType(Enum):
    RENT = 'R'
    SALE = 'S'
