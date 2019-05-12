class User:
    """
    Class that generates new instances of the user.
    """
    user_details=[]; #empty user details

    def __init__(self, username,password,email):
        self.username=username
        self.password=password
        self.email=email

    def create(self):
        User.user_details.append(self)
    def delete(self):
        User.user_details.remove(self)

    @classmethod
    def find_by_accountName(cls,number):
        for user in cls.user_details:
            if user.username==number:
                return user

    @classmethod
    def check_account_existence(cls,number):
        for user in cls.user_details:
            if user.username==number:
                return True;
        return False

    @classmethod
    def display_user(cls):
        return cls.user_details
