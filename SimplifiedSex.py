from enum import Enum

class SimplifiedSex(Enum):
    """
        SimplifiedSex enum contains the simplified binary sex for a person (this should not be treated as their gender and does not account for intersex people either) 
    """
    MALE : str = "male"
    FEMALE : str = "female"