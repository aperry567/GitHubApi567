import unittest
from HW04aperry567 import github_id
from HW04aperry567 import github_repo

def github_id(username):       
    return github_repo(username,repo) == username,repo

#Unittest case:
class github_idTest(unittest.TestCase):
    def test_github_id(self):
        #self.assertEqual(github_repo(len(username) == (8)))
        self.assertFalse(github_repo(username, repo) == (8))

"""        
class github_repoTest(unittest.TestCase):
    def test_github_repo(self):
        self.assertEqual(github_repo(username,repo) == ('aperry567','Triangle567'))
"""

username = "aperry567"
repo = "Triangle567"


#UnitTest function 
def main():
    '''main() function'''
          
if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
    main() 