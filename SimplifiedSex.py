# This class is extremely simple
# It contains the enum which represents the sex of a person

from enum import Enum

class SimplifiedSex(Enum):
    """
        SimplifiedSex enum contains the simplified binary sex for a person (this should not be treated as their gender and does not account for intersex people either) 
    """
    MALE : str = "male"
    FEMALE : str = "female"