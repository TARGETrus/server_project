from enum import Enum


class OwnerClass(Enum):
    OWNER = 'O'
    PHYSICAL_ENTITY = 'P'
    LEGAL_ENTITY = 'L'


class OwnerGender(Enum):
    MALE = 'M'
    FEMALE = 'F'


class RealEstateClass(Enum):
    REAL_ESTATE = 'E'
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


class DealClass(Enum):
    DEAL = 'D'
    RENT = 'R'
    SALE = 'S'
