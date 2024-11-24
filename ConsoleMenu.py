from typing import List, Optional, Tuple
from FamilyTree import FamilyTree
from CreateTree import create_populated_family_tree
from Person import Person

class ConsoleMenu:
    """ConsoleMenu class represents the console menu for the family tree"""
    def __init__(self):
        """
            Create a console menu and initialise the family tree and populate it
        """
        self.family_tree: FamilyTree = create_populated_family_tree()
    
    def enter_loop(self) -> None:
        """
            Enter the loop for the console menu
        """
        
        # Welcome message
        print("Family Tree Console Menu")
        print("To start, select the number corresponding to the family member you wish to view")
        ConsoleMenu.print_divider()
        
        # Loop
        while True:
            # Select a person
            person: Person = self.select_current_family_member()
            
            # Select an option to perform
            self.select_option_to_perform_person(person)
            
            # Show continue prompt
            self.prompt_continuation()
        
    @staticmethod
    def print_divider() -> None:
        """
            Print a divider to the console
        """
        print("-" * 75)
        
    def select_current_family_member(self) -> Person:
        """
            Select the family member to view their details of
            :return: the person selected
        """
        person_number: int = -1
        while person_number < 0:
            print("Please select a family member to view:")
            ConsoleMenu.print_divider()
            for person in self.family_tree.people:
                print(f"{self.family_tree.get_reference_from_person(person)+1}: {person.first_name} {person.last_name}")
            ConsoleMenu.print_divider()
            
            # Get the person
            try:
                # Get the person number and try to cast it to an int
                person_number_str = input("Person: ")
                person_number = int(person_number_str) - 1
                
                # Check number in range
                if person_number < 0 or person_number >= len(self.family_tree.people):
                    print("Out of range!")
                    person_number = -1
                    continue
                
            # Check invalid input (e.g. if a string or malformed has been given)
            except ValueError:
                print(f"Invalid input: \"{person_number_str}\"")
                person_number = -1
                continue
            # Keyboard interrupt e.g. Control + C
            except KeyboardInterrupt:
                exit(-1)
                
        return self.family_tree.get_person_from_reference(person_number)
    
    def select_option_to_perform_person(self, person: Person) -> None:
        """
            Select the option to perform on the person
            :param person: the person to perform the option on
        """
        print(f"{person.first_name} {person.last_name} has been selected.")
        ConsoleMenu.print_divider()
        print("Please select an option:")
        # Options which perform relationship look ups
        print("1: Show parents")
        print("2: Show grandchildren")
        print("3: Show immediate family")
        print("4: Show extended family")
        print("5: Show siblings")
        print("6: Show cousins")
        print("7: View calendar of everyone's birthday")
        print("8: Calculate the average age at which someone dies from deceased person")
        print("9: Calculate the average number of children per person")
        
        option_number: int = -1
        while option_number < 0:
            try:
                # Get the option
                option_number_str = input("Option: ")
                option_number = int(option_number_str)
                
                # Check number in range
                if option_number < 1 or option_number > 9:
                    print("Out of range!")
                    option_number = -1
                    continue
                
            # Check invalid input (e.g. if a string or malformed has been given)
            except ValueError:
                print(f"Invalid input: \"{option_number_str}\"")
                option_number = -1
                continue
            # Keyboard interrupt e.g. Control + C
            except KeyboardInterrupt:
                exit(-1)
                
        # Print divider
                
        # Match-case to call the appropriate option
        match option_number:
            case 1:
                self.show_parents(person)
            case 2:
                self.show_grandchildren(person)
            case 3:
                self.show_immediate_family(person)
            case 4:
                self.show_immediate_family(person, True)
            case 5:
                self.show_siblings(person)
            case 6:
                self.show_cousins(person)
            case 7:
                self.show_calendar()
            case 8:
                self.calculate_average_age_of_death()
            case 9:
                self.calculate_average_number_of_children()
            case _:
                print("Invalid option.")
                exit(-1)
    
    def prompt_continuation(self) -> None:
        """
            Prompt the user to continue or quit
        """
        print("Do you wish to continue or quit?")
        print("Please type Y to quit or N to continue.")
        # Get the input
        try:
            # Get input from the user
            prompt_number_str = input("Quit: ")
            
            # Convert the input to lowercase
            prompt_number_str = prompt_number_str.lower()
            
            if prompt_number_str == "y" or prompt_number_str == "yes":
                print("Exited program.")
                exit(0)
            
        # Keyboard interrupt e.g. Control + C
        except KeyboardInterrupt:
            exit(-1)
    
    def show_parents(self, person: Person) -> None:
        """
            Show the parents of a person
            :param person: the person to show parents of
        """
        ConsoleMenu.print_divider()
        mother: Optional[Person]
        father: Optional[Person]
        mother, father = self.family_tree.get_parents(person)
        print(f"Their mother is {mother if mother is not None else "unknown"} and their father is {father if father is not None else "unknown"}.")
        ConsoleMenu.print_divider()
        
    def show_grandchildren(self, person: Person) -> None:
        """
            Show the grandchildren of a person
            :param person: the person to show grandchildren of
            """
        ConsoleMenu.print_divider()
        grandchildren: List[Person] = self.family_tree.get_grandchildren(person)
        if grandchildren is not None and len(grandchildren) > 0:
            print("They have the following grandchildren: ", end="")
            for grandchild in grandchildren:
                print(f"{grandchild}", end="")
                # If not last grandchild, print a comma, else print full stop and line break
                if grandchild != grandchildren[-1]:
                    print(", ", end="")
                else:
                    print(".")
        else:
            print("No grandchildren found.")
        
        ConsoleMenu.print_divider()
        
    def show_immediate_family(self, person: Person, extended_family_too: bool = False) -> None:
        """
            Show the immediate family of a person and optionally the extended family
            :param person: the person to show immediate family for
            :param extended_family_too: whether to show the extended family
        """
        ConsoleMenu.print_divider()
        
        # Get spouse
        spouse: Optional[Person] = person.spouse
        parents: List[Person] = self.family_tree.get_parents(person)
        cousins: List[Person] = self.family_tree.get_children(person)
        siblings: List[Person] = self.family_tree.get_siblings(person, True)
        
        # Print the immediate family
        print(f"{person} immediate family:")
        print(f"Their spouse is {spouse if spouse is not None else 'unknown'}.")
        print(f"Mother is {parents[0] if parents[0] is not None else 'unknown'} and father is {parents[1] if parents[1] is not None else 'unknown'}.")
        print("Children are ", end="")
        
        # Iterate over the children
        if cousins is not None and len(cousins) > 0:
            for child in cousins:
                print(f"{child}", end="")
                if child != cousins[-1]:
                    print(", ", end="")
                else:
                    print(".")
        else:
            print("unknown.")
            
        # Iterate over the full siblings
        print("Full siblings are ", end="")
        full_siblings: List[Person] = siblings[0]
        if full_siblings is not None and len(full_siblings) > 0:
            for sibling in full_siblings:
                print(f"{sibling}", end="")
                if sibling != full_siblings[-1]:
                    print(", ", end="")
                else:
                    print(".")
        else:
            print("unknown.")
            
        # Iterate over the half siblings
        print("Half siblings are ", end="")
        half_siblings: List[Person] = siblings[1]
        if half_siblings is not None and len(half_siblings) > 0:
            for half_sibling in half_siblings:
                print(f"{half_sibling}", end="")
                if half_sibling != half_siblings[-1]:
                    print(", ", end="")
                else:
                    print(".")
        else:
            print("unknown.")
            
        # Extended family
        if extended_family_too:
            aunts_and_uncles: List[Person] = self.family_tree.get_aunts_and_uncles(person)
            cousins: List[Person] = self.family_tree.get_cousins(person)
            
            # Remove deceased people (if someone has a date_of_death, remove them from the list)
            cousins = [cousin for cousin in cousins if cousin.date_of_death is None]
            
            # Iterate over the aunts and uncles
            print("Aunts and uncles are ", end="")
            if aunts_and_uncles is not None and len(aunts_and_uncles) > 0:
                for aunt_and_uncle in aunts_and_uncles:
                    print(f"{aunt_and_uncle}", end="")
                    if aunt_and_uncle != aunts_and_uncles[-1]:
                        print(", ", end="")
                    else:
                        print(".")
            else:
                print("unknown.")
                
            # Iterate over the cousins
            print("Cousins are ", end="")
            if cousins is not None and len(cousins) > 0:
                for cousin in cousins:
                    print(f"{cousin}", end="")
                    if cousin != cousins[-1]:
                        print(", ", end="")
                    else:
                        print(".")
            else:
                print("unknown.")
        
        ConsoleMenu.print_divider()
        
    def show_siblings(self, person: Person) -> None:
        """
            Show the siblings of a person
            :param person: the person to show siblings for
        """
        ConsoleMenu.print_divider()
        
        # Get the siblings
        siblings: List[Person] = self.family_tree.get_siblings(person)[0]
        
        # Print the siblings
        if siblings is not None and len(siblings) > 0:
            print(f"{person} has the following siblings: ", end="")
            for sibling in siblings:
                print(f"{sibling}", end="")
                if sibling != siblings[-1]:
                    print(", ", end="")
                else:
                    print(".")
        else:
            print("No siblings found.")
            
        ConsoleMenu.print_divider()
        
    def show_cousins(self, person: Person) -> None:
        """
            Show the cousins of a person
            :param person: the person to show cousins for
        """
        ConsoleMenu.print_divider()
        
        # Get the cousins
        cousins: List[Person] = self.family_tree.get_cousins(person)
        
        # Print the cousins
        if cousins is not None and len(cousins) > 0:
            print(f"{person} has the following cousins: ", end="")
            for cousin in cousins:
                print(f"{cousin}", end="")
                if cousin != cousins[-1]:
                    print(", ", end="")
                else:
                    print(".")
        else:
            print("No cousins found.")
            
        ConsoleMenu.print_divider()
        
    def show_calendar(self) -> None:
        """
            Show the calendar of everyone's birthday in the family tree
        """
        ConsoleMenu.print_divider()
        
        # Display the birthdays in order for everyone
        birthdays: List[Tuple[Person, int, int]] = self.family_tree.get_birthdays()
        
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
                combined.append(f"{birthdays[i][1]}/{birthdays[i][2]}: {birthdays[i][0]}")
            
            # Update previous birthday 
            previous_birthday = (birthdays[i][2], birthdays[i][1])
            
        # Print the combined birthdays
        print("Birthday calendar:")
        for birthday in combined:
            print(birthday)
            
        ConsoleMenu.print_divider()
        
    def calculate_average_age_of_death(self) -> None:
        """
            Calculate the average age at which someone dies from deceased people in the family tree
        """
        ConsoleMenu.print_divider()
        
        # Get a list of all deceased people people and calculate the average age at which someone dies
        combined_age: int = 0
        deceased_people: List[Person] = self.family_tree.get_deceased()
        number_of_deceased: int = len(deceased_people)
        combined_age = sum([person.date_of_death.year - person.date_of_birth.year for person in deceased_people]) / number_of_deceased
        print(f"Of all {number_of_deceased} deceased people, the average age at which someone dies is {combined_age:.0f} years.")   
        
        ConsoleMenu.print_divider()
        
    def calculate_average_number_of_children(self) -> None:
        """
            Calculate the average number of children someone has
        """
        
        ConsoleMenu.print_divider()
        
        print("Number of children:")
        number_of_children: int = 0
        number_of_children_in_whole_tree: int = 0
        for i in range(len(self.family_tree.people)):
            number_of_children = len(self.family_tree.get_children(self.family_tree.people[i]))
            number_of_children_in_whole_tree += number_of_children
            children_plurality = "children" if number_of_children != 1 else "child"
            print(f"{self.family_tree.people[i]} has {number_of_children} {children_plurality}.")
        
        ConsoleMenu.print_divider()
        
        print(f"The average number of children is {number_of_children_in_whole_tree / len(self.family_tree.people):.4f}.")
        
        ConsoleMenu.print_divider()