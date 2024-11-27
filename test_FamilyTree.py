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
        # Test Cornelia Emmersohn
        grandparents: Tuple[Tuple[Optional[Person], Optional[Person]], Tuple[Optional[Person], Optional[Person]]] = self.family_tree.get_grandparents(self.family_tree.get_person_from_reference(22))
        self.assertNotEqual(grandparents[0], (None, None))
        self.assertNotEqual(grandparents[1], (None, None))
        
        # Test Lester Elderson-Copper
        grandparents: Tuple[Tuple[Optional[Person], Optional[Person]], Tuple[Optional[Person], Optional[Person]]] = self.family_tree.get_grandparents(self.family_tree.get_person_from_reference(1))
        self.assertEqual(grandparents[0], (None, None))
        self.assertEqual(grandparents[1], (None, None))
        
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
    
    def test_get_children(self):
        # Test Otto Emmersohn
        children: List[Person] = self.family_tree.get_children(self.family_tree.get_person_from_reference(23))
        self.assertEqual(len(children), 0)
        
        # Test Bexton Elderson-Copper
        children = self.family_tree.get_children(self.family_tree.get_person_from_reference(9))
        self.assertEqual(len(children), 1)
    
    def test_get_cousins(self):
        # Test Cornelia Emmersohn
        cousins: List[Person] = self.family_tree.get_cousins(self.family_tree.get_person_from_reference(20))
        self.assertEqual(len(cousins), 0)
        
        # Test Lester Elderson-Copper
        cousins = self.family_tree.get_cousins(self.family_tree.get_person_from_reference(1))
        self.assertEqual(len(cousins), 0)
    
    def test_get_aunts_and_uncles(self):
        # Test Cornelia Emmersohn
        aunts_and_uncles: List[Person] = self.family_tree.get_aunts_and_uncles(self.family_tree.get_person_from_reference(23))
        self.assertEqual(len(aunts_and_uncles), 0)
        
        # Test Bexton Elderson-Copper
        aunts_and_uncles = self.family_tree.get_aunts_and_uncles(self.family_tree.get_person_from_reference(9))
        self.assertEqual(len(aunts_and_uncles), 0)
    
    def test_grandchildren(self):
        # Test Adam Elderson-Copper
        grandchildren: List[Person] = self.family_tree.get_grandchildren(self.family_tree.get_person_from_reference(0))
        self.assertEqual(grandchildren, [])
        
        # Test Lester Elderson-Copper
        grandchildren = self.family_tree.get_grandchildren(self.family_tree.get_person_from_reference(1))
        self.assertEqual(len(grandchildren), 1)
    
    def test_get_deceased(self):
        # Test number of deceased
        self.assertEqual(len(self.family_tree.get_deceased()), 3)
    
    def test_get_birthdays(self):
        # Test number of birthdays
        self.assertEqual(len(self.family_tree.get_birthdays()), 25)