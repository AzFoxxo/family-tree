#!/usr/bin/env python

from typing import List, Optional, Tuple
from CreateTree import create_populated_family_tree
from FamilyTree import FamilyTree
from Person import Person

if __name__ == '__main__':
    family_tree : FamilyTree = create_populated_family_tree()
    
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
        person: Person = family_tree.get_person_from_reference(person_number)
        
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
            
        # Display the person's aunts and uncles
        aunts_and_uncles: List[Person] = family_tree.get_aunts_and_uncles(person)
        if aunts_and_uncles is not None:
            print("They have the following aunts and uncles:")
            for aunt_or_uncle in aunts_and_uncles:
                print(f" - {aunt_or_uncle}")
            
        # Display the person's cousins
        cousins: List[Person] = family_tree.get_cousins(person)
        if cousins is not None:
            print("They have these cousins:")
            for cousin in cousins:
                print(f" - {cousin}")
        else:
            print("No cousins found.")
            
        # Display the birthdays in order for everyone
        birthdays: List[Tuple[Person, int, int]] = family_tree.get_birthdays()
        
        # Sort the birthdays by month and day
        birthdays.sort(key=lambda x: (x[1], x[2]))
        
        # If two or more people share a birthday. combine them
        combined: List[str] = []
        previous_birthday: Tuple[int, int] = (-1, -1)
        for i in range(len(birthdays)):
            # Check is previous birthday
            if previous_birthday == (birthdays[i][1], birthdays[i][2]):
                combined[-1] += f", {birthdays[i][0]}"
            else:
                # Add the person and their birthday
                combined.append(f"{birthdays[i][0]}: {birthdays[i][1]}/{birthdays[i][2]}")
            
            # Update previous birthday 
            previous_birthday = (birthdays[i][2], birthdays[i][1])
            
        # Print the combined birthdays
        print("Birthday calendar:")
        for birthday in combined:
            print(birthday)
            
            
        # Calculate the average age of a person
        combined_age: int = 0
        deceased_people: List[Person] = family_tree.get_deceased()
        number_of_deceased: int = len(deceased_people)
        combined_age = sum([person.DOD.year - person.DOB.year for person in deceased_people]) / number_of_deceased
        print(f"Of all {number_of_deceased} deceased people, the average age at which someone dies is {combined_age:.0f} years.")        
        
        # Find of the number of children for each person and overall total
        print("Number of children:")
        number_of_children: int = 0
        number_of_children_in_whole_tree: int = 0
        for i in range(len(family_tree.people)):
            number_of_children = len(family_tree.get_children(family_tree.people[i]))
            number_of_children_in_whole_tree += number_of_children
            children_plurality = "children" if number_of_children != 1 else "child"
            print(f"{family_tree.people[i]} has {number_of_children} {children_plurality}.")
            
        print(f"The average number of children is {number_of_children_in_whole_tree / len(family_tree.people):.4f}.")
        
        break