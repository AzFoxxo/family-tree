#!/usr/bin/env python

from typing import List, Optional, Tuple
from CreateTree import create_populate_family_tree
from FamilyTree import FamilyTree
from Person import Person

if __name__ == '__main__':
    family_tree : FamilyTree = create_populate_family_tree()
    
    while True:
        print("Enter the number of the person to find their relationships:")
        
        # List all people
        print("-" * 75)
        for person in family_tree.people:
            print(f"{family_tree.get_reference_from_person(person)+1}: {person.fname} {person.lname}")
        print("-" * 75)
        
        # Get the person
        try:
            # Get the person number and try to cast it to an int
            person_number_str = input("Person: ")
            person_number = int(person_number_str) - 1
            
            # Check number in range
            if person_number < 0 or person_number >= len(family_tree.people):
                print("Invalid person number!")
                continue
            
        # Check invalid input (e.g. if a string or malformed has been given)
        except ValueError:
            print(f"Invalid input: \"{person_number_str}\"")
            continue
        # Keyboard interrupt e.g. Control + C
        except KeyboardInterrupt:
             exit(-1)
        
        # Get the person from the person reference
        person = family_tree.get_person_from_reference(person_number)
        
        # Show basic information about the person
        print(f"{person.fname} {person.lname} is {person.sex.value}.")
        print(f"Their spouse is {person.spouse if person.spouse is not None else 'not set or are not yet married'}.")
        
        # Print parents' names
        mother: Optional[Person]
        father: Optional[Person]
        mother, father = family_tree.get_parents(person)
        print(f"Their mother is {mother if mother is not None else "unknown"} and their father is {father if father is not None else "unknown"}.")
        
        # Print the grandparents's names
        grandparents: Tuple[Tuple[Optional[Person], Optional[Person]], Tuple[Optional[Person], Optional[Person]]] = family_tree.get_grandparents(person)
        print(f"Their mum's grandparents are {grandparents[0][0] if grandparents[0][0] is not None else 'unknown'} and {grandparents[0][1] if grandparents[0][1] is not None else 'unknown'}.")
        print(f"Their dad's grandparents are {grandparents[1][0] if grandparents[1][0] is not None else 'unknown'} and {grandparents[1][1] if grandparents[1][1] is not None else 'unknown'}.")
        
        # Print the siblings' names
        siblings: Tuple[List[Person], List[Person]] = family_tree.get_siblings(person, True)
        if siblings is not None:
            # Full siblings
            if len(siblings[0]) > 0:
                print("They have these siblings:")
                for sibling in siblings[0]:
                    print(f" - {sibling.fname} {sibling.lname}")
            else:
                print("No full siblings found.")
                
            # Half siblings
            if len(siblings[1]) > 0:
                print("They have the following half siblings:")
                for sibling in siblings[1]:
                    print(f" - {sibling.fname} {sibling.lname}")
            else:
                print("No half siblings found.")
                
        # Display the person's children
        children: List[Person] = family_tree.get_children(person)
        if children is not None:
            print("They have the following children:")
            for child in children:
                print(f" - {child}")
        else:
            print("No children found.")
            
        # Display the person's grandchildren
        grandchildren: List[Person] = family_tree.get_grandchildren(person)
        if children is not None:
            print("They have the following grandchildren:")
            for grandchild in grandchildren:
                print(f" - {grandchild}")
        else:
            print("No grandchildren found.")
            
        # Display the person's cousins
        cousins: List[Person] = family_tree.get_cousins(person)
        if cousins is not None:
            print("They have these cousins:")
            for cousin in cousins:
                print(f" - {cousin}")
        else:
            print("No cousins found.")
        
        break