#!/usr/bin/env python

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