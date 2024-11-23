from typing import Optional, Self
import SimplifiedSex


"""Person class which represents all people within the family tree"""
class Person:
    def __init__(self, fname: str, lname: str, sex : SimplifiedSex, mother: Optional[Self] = None, father: Optional[Self] = None):
        self.fname: str = fname
        self.lname: str = lname
        self.sex : SimplifiedSex = sex
        self.mother: Optional[Self] = mother
        self.father: Optional[Self] = father
        self.spouse: Optional[Self] = None
    
    # Print the name of the person when Person is printed
    def __str__(self): return f'{self.fname} {self.lname}'