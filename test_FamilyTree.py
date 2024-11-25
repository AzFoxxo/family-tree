#!/usr/bin/python

from typing import Optional, Tuple
import unittest

from CreateTree import create_populated_family_tree
from FamilyTree import FamilyTree
from Person import Person

class FamilyTreeTesting(unittest.TestCase):
    # Unit test setup
    def setUp(self):
        self.family_tree: FamilyTree = create_populated_family_tree()
    
    def test_get_parents(self):
        # Adam Elderson-Copper
        self.assertEqual(self.family_tree.get_parents(self.family_tree.get_person_from_reference(0)), (None, None))
        
        # Bexton Elderson-Copper
        result: Tuple[Optional[Person], Optional[Person]] = self.family_tree.get_parents(self.family_tree.get_person_from_reference(9))
        if result[0] is not None:
            self.assertEqual(result[0].first_name, "Amber")
        if result[1] is not None:
            self.assertEqual(result[1].first_name, "Lester")
            
    def test_get_grandparents(self):
        pass
    
    def test_get_siblings(self):
        pass
    
    def test_get_children(self):
        pass
    
    def test_get_cousins(self):
        pass
    
    def test_get_aunts_and_uncles(self):
        pass
    
    def test_grandchildren(self):
        pass
    
    def test_get_deceased(self):
        pass
    
    def test_get_birthdays(self):
        pass