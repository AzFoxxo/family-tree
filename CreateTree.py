import datetime
from FamilyTree import FamilyTree
from Person import Person
from SimplifiedSex import SimplifiedSex

def create_populated_family_tree() -> FamilyTree:
    """
        Create the family tree and populate it with data (loader)
        :return: the populated family tree
    """
    # Create the empty family tree
    family_tree: FamilyTree = FamilyTree()

    # Populate the family tree

    #region First generation
    # Adam and Jasmine
    adam: int = family_tree.add_person(Person("Adam", "Wax", SimplifiedSex.MALE, datetime.date(1920, 5, 24)))
    jasmine: int = family_tree.add_person(Person("Jasmine", "Wax", SimplifiedSex.FEMALE, datetime.date(1926, 4, 10)))
    family_tree.set_partner(adam, jasmine)
    
    # Stew and Amber
    stew: Person = family_tree.add_person(Person("Stew", "Knotberry", SimplifiedSex.MALE, datetime.date(1930, 6, 6)))
    eve: Person = family_tree.add_person(Person("Eve", "Knotberry", SimplifiedSex.FEMALE, datetime.date(1924, 6, 6)))
    family_tree.set_partner(stew, eve)
    
    # Mark deceased people
    adam.set_deceased(datetime.date(1991, 4, 12))
    jasmine.set_deceased(datetime.date(1994, 11, 3))
    eve.set_deceased(datetime.date(2003, 2, 20))
    
    #endregion
    
    #region Second generation
    # Amber and Stew's children
    john: Person = family_tree.add_person(Person("John", "Knotberry", SimplifiedSex.MALE, datetime.date(1950, 3, 3), jasmine, adam))
    mary: Person = family_tree.add_person(Person("Mary", "Knotberry", SimplifiedSex.FEMALE, datetime.date(1951, 12, 29), jasmine, adam))
    lester: Person = family_tree.add_person(Person("Lester", "Knotberry", SimplifiedSex.MALE, datetime.date(1952, 2, 28), jasmine, adam))
    
    # Adam and Jasmine's children
    jedward: Person = family_tree.add_person(Person("Jedward", "Wax", SimplifiedSex.MALE, datetime.date(1950, 5, 25), eve, stew))
    jenna: Person = family_tree.add_person(Person("Jenna", "Wax", SimplifiedSex.MALE, datetime.date(1952, 4, 2), eve, stew))
    
    # Amber and Stew's grandchildren
    harry: Person = family_tree.add_person(Person("Harry", "Wax", SimplifiedSex.MALE, datetime.date(1948, 2, 28), eve, adam))
    
    # Partner second generation
    family_tree.set_partner(lester, jedward)
    family_tree.set_partner(jenna, john)
    
    #endregion
    
    #region Third generation
    # John and Jenna's children
    jackson: Person = family_tree.add_person(Person("Jackson", "Knotberry-Wax", SimplifiedSex.MALE, datetime.date(1970, 5, 3), jenna, john))
    Wirral: Person = family_tree.add_person(Person("Wirral", "Knotberry-Wax", SimplifiedSex.FEMALE, datetime.date(1973, 3, 17), jenna, john))
    Paxton: Person = family_tree.add_person(Person("Paxton", "Knotberry-Wax", SimplifiedSex.MALE, datetime.date(1976, 5, 3), jenna, john))
    
    #endregion
    
    return family_tree