from enum import Enum

"""SimplifiedSex Enum contains the simplified binary sex for a person (gender identity not included or intersex classification)"""
class SimplifiedSex(Enum):
    MALE : str = "male"
    FEMALE : str = "female"