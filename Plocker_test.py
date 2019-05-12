from Plocker import User
import unittest
class UserTest(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    #test 1
    def tearDown(self):
        '''
        This function ensures that each time the test runs it runs afresh without memory of the previous details
        '''
        User.user_details=[]
    def setUp(self):
        """
        This is a set up function that runs every time before each test clauses
        """

        #checks for user details
        self.user_details=User("IanBTrey","Manchester44","kibetkirui010@gmail.com")
    #test 2
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.user_details.username,"IanBTrey")
        self.assertEqual(self.user_details.password,"Manchester44")
        self.assertEqual(self.user_details.email,"kibetkirui010@gmail.com")
