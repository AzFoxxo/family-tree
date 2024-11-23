"""Create the family tree"""

from FamilyTree import FamilyTree
from Person import Person
from SimplifiedSex import SimplifiedSex

def create_populate_family_tree() -> FamilyTree:
    family_tree = FamilyTree()
    
    # Create the empty family tree
    family_tree: FamilyTree = FamilyTree()

    # Populate the family tree

    #region First generation
    # Adam and Jasmine
    adam: int = family_tree.add_person(Person("Adam", "Wax", SimplifiedSex.MALE, None, None)) 
    jasmine: int = family_tree.add_person(Person("Jasmine", "Wax", SimplifiedSex.FEMALE, None, None))
    family_tree.partner(adam, jasmine)
    
    # Stew and Amber
    stew: Person = family_tree.add_person(Person("Stew", "Wax", SimplifiedSex.MALE, None, None)) 
    amber: Person = family_tree.add_person(Person("Amber", "Wax", SimplifiedSex.FEMALE, None, None))
    family_tree.partner(stew, amber)
    
    #endregion
    
    #region Second generation
    # Amber and Stew's children
    john: Person = family_tree.add_person(Person("John", "Wax", SimplifiedSex.MALE, jasmine, adam))
    mary: Person = family_tree.add_person(Person("Mary", "Wax", SimplifiedSex.FEMALE, jasmine, adam))
    lester: Person = family_tree.add_person(Person("Lester", "Wax", SimplifiedSex.MALE, jasmine, adam))
    
    # Adam and Jasmine's children
    jedward: Person = family_tree.add_person(Person("Jedward", "Wax", SimplifiedSex.MALE, amber, stew))
    jenna: Person = family_tree.add_person(Person("Jenna", "Wax", SimplifiedSex.MALE, amber, stew))
    
    # Amber and Stew's grandchildren
    harry: Person = family_tree.add_person(Person("Harry", "Wax", SimplifiedSex.MALE, amber, adam))
    
    # Partner second generation
    family_tree.partner(lester, jedward)
    family_tree.partner(jenna, john)
    
    #endregion
    
    #region Third generation
    # John and Jenna's children
    jackson: Person = family_tree.add_person(Person("Jackson", "Wax", SimplifiedSex.MALE, jenna, john))
    Wirral: Person = family_tree.add_person(Person("Wirral", "Wax", SimplifiedSex.FEMALE, jenna, john))
    Paxton: Person = family_tree.add_person(Person("Paxton", "Wax", SimplifiedSex.MALE, mary, john))
    
    # Harry and Mary's children
    luke: Person = family_tree.add_person(Person("Bexton", "Wax", SimplifiedSex.MALE, mary, harry))
    
    #endregion
    return family_tree