#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from howdoi import *

class TestHowDoI(unittest.TestCase):

    def test_is_question_with_empty_string_is_false(self):
        self.assertFalse(is_question(""))

    def test_is_question(self):
        self.assertTrue(is_question("/questions/2323/tototutu"))

    def test_get_link_at_pos(self):
        self.assertEquals('/questions/1234/', get_link_at_pos(["/questions/1234/"], 1))
        self.assertEquals('/questions/1234/', get_link_at_pos(["/questions/1234/"], 2))
        self.assertEquals('/questions/1234/', get_link_at_pos(["/tutu", "/questions/1234/"], 1))
        self.assertEquals('/questions/1234/', get_link_at_pos(["/questions/1234/", "/questions/12043/"], 1))

if __name__ == '__main__':
    dir()
    unittest.main()

