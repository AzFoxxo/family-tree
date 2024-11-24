"""Create the family tree"""

from FamilyTree import FamilyTree
from Person import Person
from SimplifiedSex import SimplifiedSex

def create_populate_family_tree() -> FamilyTree:
    # Create the empty family tree
    family_tree: FamilyTree = FamilyTree()

    # Populate the family tree

    #region First generation
    # Adam and Jasmine
    adam: int = family_tree.add_person(Person("Adam", "Wax", SimplifiedSex.MALE, None, None)) 
    jasmine: int = family_tree.add_person(Person("Jasmine", "Wax", SimplifiedSex.FEMALE, None, None))
    family_tree.partner(adam, jasmine)
    
    # Stew and Amber
    stew: Person = family_tree.add_person(Person("Stew", "Knotberry", SimplifiedSex.MALE, None, None)) 
    eve: Person = family_tree.add_person(Person("Eve", "Knotberry", SimplifiedSex.FEMALE, None, None))
    family_tree.partner(stew, eve)
    
    #endregion
    
    #region Second generation
    # Amber and Stew's children
    john: Person = family_tree.add_person(Person("John", "Knotberry", SimplifiedSex.MALE, jasmine, adam))
    mary: Person = family_tree.add_person(Person("Mary", "Knotberry", SimplifiedSex.FEMALE, jasmine, adam))
    lester: Person = family_tree.add_person(Person("Lester", "Knotberry", SimplifiedSex.MALE, jasmine, adam))
    
    # Adam and Jasmine's children
    jedward: Person = family_tree.add_person(Person("Jedward", "Wax", SimplifiedSex.MALE, eve, stew))
    jenna: Person = family_tree.add_person(Person("Jenna", "Wax", SimplifiedSex.MALE, eve, stew))
    
    # Amber and Stew's grandchildren
    harry: Person = family_tree.add_person(Person("Harry", "Wax", SimplifiedSex.MALE, eve, adam))
    
    # Partner second generation
    family_tree.partner(lester, jedward)
    family_tree.partner(jenna, john)
    
    #endregion
    
    #region Third generation
    # John and Jenna's children
    jackson: Person = family_tree.add_person(Person("Jackson", "Knotberry-Wax", SimplifiedSex.MALE, jenna, john))
    Wirral: Person = family_tree.add_person(Person("Wirral", "Knotberry-Wax", SimplifiedSex.FEMALE, jenna, john))
    Paxton: Person = family_tree.add_person(Person("Paxton", "Knotberry-Wax", SimplifiedSex.MALE, jenna, john))
    
    #endregion
    return family_tree