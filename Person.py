import datetime
from typing import Optional, Self
import SimplifiedSex

class Person:
    """Person class represents a person inside the family tree"""
    def __init__(self, first_name: str, last_name: str, sex: SimplifiedSex, date_of_birth: datetime.date, mother: Optional[Self] = None, father: Optional[Self] = None):
        """
            Create a new person and set their required properties
            :param first_name: first name
            :param last_name: last name
            :param sex: the simplified sex representation of the person
            :param date_of_birth: date of birth
            :param mother: person's mother
            :param father: person's father
        """
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.sex : SimplifiedSex = sex
        self.date_of_birth: datetime.date = date_of_birth
        self.mother: Optional[Self] = mother
        self.father: Optional[Self] = father
        self.spouse: Optional[Self] = None
        self.date_of_death: Optional[datetime.date] = None
    
    def __str__(self) -> str:
        """
            Returns the name of the person when person is converted to a string
            :return: person's first and last name
        """
        return f"{self.first_name} {self.last_name}"
    
    def set_deceased(self, date_of_death: datetime.date) -> None:
        """
            Set the date a person died on
            :param date_of_death: date of death
        """
        self.date_of_death = date_of_death