import unittest

from HW04aperry567 import github_id
from HW04aperry567 import github_repo


def github_id(username):
    """ Method from main program"""
    return github_repo(username, repo) == username, repo

#Unittest case:
class github_idTest(unittest.TestCase):
    def test_github_id(self):
        self.assertEqual(len(username),8)




