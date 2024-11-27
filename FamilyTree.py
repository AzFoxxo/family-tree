# This class contains all the functionality required for relationship lookups,
# Adding people to the family tree,
# Setting spouses of two people
# This class should not contain any logic not related to manipulating the family tree
# Or looking up relationships in the family tree
# User facing code e.g. printing to the terminal, should be carried out in ConsoleMenu

import datetime
from typing import List, Optional, Tuple
from Person import Person

class FamilyTree:
    """FamilyTree class stores the family tree and methods to find relationships within it"""
    def __init__(self):
        self.people = []
    
    def add_person(self, person: Person) -> Person:
        """
            Add a person to the list of people
            :param person: person to add
            :return: the person, this used so you have a reference to the person for calling code like set_partner
        """
        self.people.append(person)
        return person

    def set_partner(self, person1: Person, person2: Person) -> None:
        """
            Set two people as partners
            :param person1: first person
            :param person2: second person
        """
        person1.spouse = person2
        person2.spouse = person1
        
    def get_person_from_reference(self, person_reference: int) -> Person:
        """
            Convert a person's reference to their object
            :param person_reference: the int reference to the person in the list of people
            :return: the person object
        """
        return self.people[person_reference]
    
    def get_reference_from_person(self, person: Person) -> int:
        """
            Convert a person to their person reference
            :param person: the person object
            :return: the int reference to the person in the list of people
            """
        return self.people.index(person)
    
    def get_parents(self, person: Person) -> Tuple[Optional[Person], Optional[Person]]:
        """
            Get parents of a person
            :param person: the person to find the parents of
            :return: the mother and father of the person if they have been set
        """
        return person.mother, person.father
    
    def get_grandparents(self, person: Person) -> Tuple[Tuple[Optional[Person], Optional[Person]], Tuple[Optional[Person], Optional[Person]]]:
        """
            Get grandparents of a person
            :param person: the person to find the grandparents of
            :return: the grandparents of the person in the order in the following format (mother's mother, mother's father), (father's mother, father's father)
        """
        mother, father = self.get_parents(person)
        mother_parents: Tuple[Optional[Person], Optional[Person]] = (None, None)
        father_parents: Tuple[Optional[Person], Optional[Person]] = (None, None)
        
        # Get mother's parents
        if mother is not None:
            mother_parents = self.get_parents(mother)
            
        # Get father's parents
        if father is not None:
            father_parents = self.get_parents(father)
        
        return mother_parents, father_parents
       
    
    def get_siblings(self, person: Person, include_half_siblings: bool = False) -> Tuple[List[Person], List[Person]]:
        """
            Get siblings of a person
            :param person: the person to find the siblings of
            :param include_half_siblings: if it should include half siblings
            :return: the siblings of the person in the format (full siblings, half siblings)
        """
        siblings = []
        
        # Get parents
        mother, father = self.get_parents(person)
        
        # Get parent's children - siblings
        siblings = self.get_children(mother)
        siblings += self.get_children(father)
        
        # Remove duplicate entries
        siblings = list(dict.fromkeys(siblings))
        
        full_siblings = []
        half_siblings = []
        
        # Remove self from the list
        if person in siblings:
            siblings.remove(person)
        
        # Add to the correct list
        for sibling in siblings:
            if (sibling.mother == mother and sibling.mother != None) and (sibling.father == father and sibling.father != None):
                full_siblings.append(sibling)
            elif include_half_siblings and ((sibling.mother == mother and sibling.mother != None) or (sibling.father == father and sibling.father != None)):
                half_siblings.append(sibling)
                    
        return full_siblings, half_siblings
    
    
    def get_children(self, person: Person) -> List[Person]:
        """
            Get the children
            :param person: the person to find their children
            :return: the children of them
        """
        children: List[Person] = []
        
        # Find all children who share the faster or mother
        for i in self.people:
            if (i.mother == person and i.mother is not None) or (i.father == person and i.father is not None):
                children.append(i)
                
        return children
    
    def get_grandchildren(self, person: Person) -> List[Person]:
        """
            Get the grandchildren
            :param person: the person to find their grandchildren
            :return: the grandchildren of them
        """
        grandchildren: List[Person] = []
        children: List[Person] = self.get_children(person)
        
        for child in children:
            grandchildren.extend(self.get_children(child))
            
        # Remove duplicate entries
        grandchildren = list(dict.fromkeys(grandchildren))
        
        return grandchildren
    
    def get_aunts_and_uncles(self, person: Person) -> List[Person]:
        """
            Find aunts or uncles
            :param person: the person to get their aunts or uncles
            :return: the aunts or uncles of the person
        """
        parents: Tuple[Optional[Person], Optional[Person]] = self.get_parents(person)
        mother: Person = parents[0]
        father: Person = parents[1]
        aunts_and_uncles = []
        
        # Get mother's siblings
        if mother is not None:
            for i in self.get_siblings(mother, True)[0]:
                aunts_and_uncles.append(i)
        
        # Get father's siblings
        if father is not None:
            for i in self.get_siblings(father, True)[0]:
                aunts_and_uncles.append(i)
                    
        return aunts_and_uncles
    
    def get_cousins(self, person: Person) -> List[Person]:
        """
            Find all the cousins of them
            :param person: the person to find their cousins
            :return: the cousins of them
        """
        parents: Tuple[Optional[Person], Optional[Person]] = self.get_parents(person)
        mother: Person = parents[0]
        father: Person = parents[1]
        aunts_and_uncles: List[Person] = self.get_aunts_and_uncles(person)
        cousins = []
        
        for aunt_or_uncle in aunts_and_uncles:
            cousins += self.get_children(aunt_or_uncle)
        
        return cousins
    
    def get_birthdays(self) -> List[Tuple[Person, int, int]]:
        """
            Return a list of everyone's birthdays
            :return: a list containing a tuple of the Person's who birthday it is, the month and the day of their birthday
        """
        birthdays: List[Tuple[Person, int, int]] = []
        for i in self.people:
            birthdays.append((i, i.date_of_birth.month, i.date_of_birth.day))
            
        return birthdays
    
    def get_deceased(self) -> List[Person]:
        """
            Return a list of deceased people
            :return: a list of people who are deceased
        """
        deceased: List[Person] = []
        for i in self.people:
            if i.date_of_death is not None:
                deceased.append(i)
                
        return deceased