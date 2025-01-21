import getpass

class Voter:
    voters_db = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.has_voted = False

    @classmethod
    def add_voter(cls, username, password):
        if username in cls.voters_db:
            print("Username already exists. Please try a different username.")
            return False
        cls.voters_db[username] = Voter(username, password)
        return True

    @classmethod
    def authenticate(cls, username, password):
        voter = cls.voters_db.get(username)
        if voter and voter.password == password:
            return voter
        return None

def register_voter():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    if Voter.add_voter(username, password):
        print("Voter registered successfully.")
    else:
        print("Registration Failed.")

def login_voter():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ")
    voter = Voter.authenticate(username, password)
    if voter:
        print("Login successful.")
    else:
        print("Invalid username or password.")
