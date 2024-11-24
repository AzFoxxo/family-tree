from typing import List, Optional, Tuple
from Person import Person

"""FamilyTree class stores the family tree and methods to find relationships within it"""
class FamilyTree:
    def __init__(self):
        self.people = []
    
    """Add a person to the list of people"""
    def add_person(self, person: Person) -> Person:
        self.people.append(person)
        return person

    """Partner a person with another person - mark as spouses"""
    def set_partner(self, person1: Person, person2: Person) -> None:
        person1.spouse = person2
        person2.spouse = person1
        
    """Convert a person's reference to their object"""
    def get_person_from_reference(self, person_reference: int) -> Person:
        return self.people[person_reference]
    
    """Convert a person to their person reference"""
    def get_reference_from_person(self, person: Person) -> int:
        return self.people.index(person)
    
    """Get parents of a person"""
    def get_parents(self, person: Person) -> Tuple[Optional[Person], Optional[Person]]:
        return person.mother, person.father
    
    """
    Get grandparents of a person
    Returns mother's parents first and then the father's parents e.g.
    (mother's mother, mother's father), (father's mother, father's father)
    """
    def get_grandparents(self, person: Person) -> Tuple[Tuple[Optional[Person], Optional[Person]], Tuple[Optional[Person], Optional[Person]]]:
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
       
    
    """Get siblings of a person"""
    def get_siblings(self, person: Person, include_half_siblings: bool = False) -> Tuple[List[Person], List[Person]]:
        siblings = []
        half_siblings = []
        mother, father = self.get_parents(person)
        
        # Check for siblings
        for i in self.people:
            # Get all full siblings
            if i.mother == mother and i.father == father and i.mother != None and i.father != None:
                if i is not person:
                    siblings.append(i)
            # Get all half siblings
            elif include_half_siblings and (i.mother == mother or i.father == father):
                if i is not person:
                    half_siblings.append(i)
                    
        return siblings, half_siblings
    
    
    """Get the children"""
    def get_children(self, person: Person) -> List[Person]:
        children: List[Person] = []
        
        for i in self.people:
            if i.mother == person or i.father == person:
                children.append(i)
                
        return children
    
    """Get the grandchildren"""
    def get_grandchildren(self, person: Person) -> List[Person]:
        grandchildren: List[Person] = []
        children: List[Person] = self.get_children(person)
        
        for child in children:
            grandchildren.extend(self.get_children(child))
            
        # Remove duplicate entries
        grandchildren = list(dict.fromkeys(grandchildren))
        
        return grandchildren
    
    """Find all the cousins of them"""
    def get_cousins(self, person: Person) -> List[Person]:
        parents = self.get_parents(person)
        mother = parents[0]
        father = parents[1]
        aunts_and_uncles = self.get_siblings(mother) + self.get_siblings(father) 
        cousins = []
        
        for aunt_or_uncle in aunts_and_uncles:
            cousins += self.get_children(aunt_or_uncle)
        
        return cousins