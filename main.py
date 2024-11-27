#!/usr/bin/env python

# This file is the entry point for the program
# It should not contain any code except that responsible
# for creating the console menu and entering the loop

from ConsoleMenu import ConsoleMenu

def console_interface_entry() -> None:
    """
        Create and enter CLI loop
    """
    
    # Create the console menu and enter menu loop 
    console_menu: ConsoleMenu = ConsoleMenu()
    console_menu.enter_loop()

if __name__ == '__main__':
    console_interface_entry()