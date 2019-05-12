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
    #test 3
    def create_test(self):
        '''
        create_test to test for creation of new credentials
        '''
        self.user_details.create() #create a new account/credentials
        self.assertEqual(len(User.user_details),1)
    #test 4
    def save_user_details_test(self):
        '''
        save_test to check if we can save multiple accounts/credentials in our user_details
        '''
        self.user_details.create()
        test_userDetails=User("Test","user","oceanpark@gmail.com")
        test_userDetails.create()
        self.assertEqual(len(User.user_details),2)
    #test 5
    def delete_user_details_test(self):
        '''
        delete_test to check if we can erase a credential from our account
        '''
        self.user_details.create()
        test_userDetails=User("Test","user","oceanpark@gmail.com")
        test_userDetails.create()

        self.user_details.delete_password() # deletes a password
        self.assertEqual(len(User.user_details),1)
    #test 6
    def find_by_accountName_test(self):
        '''
        find_test to search for a particular account and display them
        '''
        self.user_details.create()
        test_userDetails=User("Test","user","oceanpark@gmail.com")
        test_userDetails.create()

        found_account=User.find_by_accountName("Test")
        self.assertEqual(found_account.username,test_userDetails.username)

    #test 7
    def check_account_existence_test(self):
        '''
        check_account_existence_test to check for the existence of an account
        '''
        self.user_details.create()
        test_userDetails=User("Test","user","oceanpark@gmail.com")
        test_userDetails.create()

        account_exist=User.check_account_existence("Test")
        self.assertTrue(account_exist)
