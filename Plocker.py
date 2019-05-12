class User:
    """
    Class that generates new instances of the user.
    """
    user_details=[]; #empty user details

    def __init__(self, username,password,email):
        self.username=username
        self.password=password
        self.email=email
