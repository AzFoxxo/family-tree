#!/usr/bin/python

from typing import List, Optional, Tuple
import unittest

from CreateTree import create_populated_family_tree
from FamilyTree import FamilyTree
from Person import Person

class FamilyTreeTesting(unittest.TestCase):
    # Unit test setup
    def setUp(self):
        self.family_tree: FamilyTree = create_populated_family_tree()
    
    def test_get_parents(self):
        # Test Adam Elderson-Copper
        self.assertEqual(self.family_tree.get_parents(self.family_tree.get_person_from_reference(0)), (None, None))
        
        # Test Bexton Elderson-Copper
        result: Tuple[Optional[Person], Optional[Person]] = self.family_tree.get_parents(self.family_tree.get_person_from_reference(9))
        if result[0] is not None:
            self.assertEqual(result[0].first_name, "Amber")
        if result[1] is not None:
            self.assertEqual(result[1].first_name, "Lester")
            
    def test_get_grandparents(self):
        pass
    
    def test_get_siblings(self):
        # Test Carol Boulder
        siblings: Tuple[List[Person], List[Person]] = self.family_tree.get_siblings(self.family_tree.get_person_from_reference(2))
        self.assertEqual(len(siblings[0]), 0)
        self.assertEqual(len(siblings[1]), 0)
        
        # Test Angel Eyre
        siblings = self.family_tree.get_siblings(self.family_tree.get_person_from_reference(19))
        self.assertEqual(len(siblings[0]), 1)
        self.assertEqual(len(siblings[1]), 0)

        # Test Angel Eyre - Include half siblings
        siblings = self.family_tree.get_siblings(self.family_tree.get_person_from_reference(19), True)
        self.assertEqual(len(siblings[0]), 1)
        self.assertEqual(len(siblings[1]), 1)
        
        
        
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