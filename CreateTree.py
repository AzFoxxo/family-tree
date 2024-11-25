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
    
    #region Generation #1
    adam: Person = Person("Adam", "Elderson-Copper", SimplifiedSex.MALE, datetime.date(1943, 3, 23))
    lester: Person = Person("Lester", "Elderson-Copper", SimplifiedSex.MALE, datetime.date(1945, 5, 12))
    family_tree.add_person(adam)
    family_tree.add_person(lester)
    family_tree.set_partner(adam, lester)
    
    amber: Person = Person("Amber", "Copper", SimplifiedSex.FEMALE, datetime.date(1943, 3, 23))
    family_tree.add_person(amber)
    
    thomas: Person = Person("Thomas", "Emmersohn", SimplifiedSex.MALE, datetime.date(1943, 3, 23))
    ginny: Person = Person("Ginny", "Emmersohn", SimplifiedSex.FEMALE, datetime.date(1944, 7, 8))
    family_tree.add_person(thomas)
    family_tree.add_person(ginny)
    family_tree.set_partner(thomas, ginny)
    
    john: Person = Person("John", "Colder", SimplifiedSex.MALE, datetime.date(1930, 5, 2))
    jeanette: Person = Person("Jeanette", "Colder", SimplifiedSex.FEMALE, datetime.date(1939, 6, 12))
    family_tree.add_person(john)
    family_tree.add_person(jeanette)
    family_tree.set_partner(john, jeanette)
    
    # Mark people as deceased
    john.set_deceased(datetime.date(1990, 3, 23))
    jeanette.set_deceased(datetime.date(1990, 3, 23))
    ginny.set_deceased(datetime.date(1960, 7, 2))
    
    #endregion
    
    #region Generation #2
    greg: Person = Person("Greg", "Boulder", SimplifiedSex.MALE, datetime.date(1965, 3, 23))
    carol: Person = Person("Carol", "Boulder",SimplifiedSex.FEMALE, datetime.date(1967, 5, 12))
    family_tree.add_person(greg)
    family_tree.add_person(carol)
    family_tree.set_partner(greg, carol)
    
    bexton: Person = Person("Bexton", "Elderson-Copper", SimplifiedSex.MALE, datetime.date(1965, 3, 23), amber, lester)
    family_tree.add_person(bexton)
    
    david: Person = Person("David", "Eyre", SimplifiedSex.MALE, datetime.date(1963, 4, 1))
    sandra: Person = Person("Sandra", "Eyre", SimplifiedSex.FEMALE, datetime.date(1964, 8, 12))
    family_tree.add_person(david)
    family_tree.add_person(sandra)
    family_tree.set_partner(david, sandra)
    
    jamie: Person = Person("Jamie", "Emmersohn", SimplifiedSex.MALE, datetime.date(1965, 3, 23), ginny, thomas)
    dorothy: Person = Person("Dorothy", "Emmersohn", SimplifiedSex.FEMALE, datetime.date(1967, 5, 12), jeanette, john)
    family_tree.add_person(jamie)
    family_tree.add_person(dorothy)
    family_tree.set_partner(jamie, dorothy)
    
    frank: Person = Person("Frank", "Anderson", SimplifiedSex.MALE, datetime.date(1966, 8, 8))
    jane: Person = Person("Jane", "Anderson", SimplifiedSex.FEMALE, datetime.date(1966, 8, 8))
    family_tree.add_person(frank)
    family_tree.add_person(jane)
    family_tree.set_partner(frank, jane)
    #endregion
    
    #region Generation #3
    clyde: Person = Person("Clyde", "Emmersohn", SimplifiedSex.MALE, datetime.date(1990, 3, 23), dorothy, jamie)
    bethany: Person = Person("Bethany", "Anderson", SimplifiedSex.FEMALE, datetime.date(1990, 3, 23), jane, frank)
    family_tree.add_person(clyde)
    family_tree.add_person(bethany)
    family_tree.set_partner(clyde, bethany)
    
    james: Person = Person("James", "Eyre", SimplifiedSex.MALE, datetime.date(1990, 3, 23), sandra, david)
    angie: Person = Person("Angie", "Eyre", SimplifiedSex.FEMALE, datetime.date(1992, 11, 12), carol, greg)
    family_tree.add_person(james)
    family_tree.add_person(angie)
    family_tree.set_partner(james, angie)
    
    dylan: Person = Person("Dylan", "Boulder", SimplifiedSex.MALE, datetime.date(1990, 3, 23), carol, greg)
    lee: Person = Person("Lee", "Elderson-Copper", SimplifiedSex.MALE, datetime.date(1990, 3, 23), carol, bexton)
    family_tree.add_person(dylan)
    family_tree.add_person(lee)
    #endregion
    
    #region Generation #4
    family_tree.add_person(Person("Cornelia", "Emmersohn", SimplifiedSex.FEMALE, datetime.date(2015, 3, 23), angie, james))
    family_tree.add_person(Person("Otto", "Emmersohn", SimplifiedSex.MALE, datetime.date(2010, 3, 23), bethany, clyde))
    
    return family_tree