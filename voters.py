import getpass

class Voter:
    voters_db = {}

    def __init__(self, nid, password):
        self.nid = nid
        self.password = password
        self.has_voted = False

    @classmethod
    def add_voter(cls, nid, password):
        if nid in cls.voters_db:
            print("NID already exists. Please try a different NID.")
            return False
        if len(nid) != 10 or not nid.isdigit():
            print("Invalid NID. NID must be a 10-digit number.")
            return False
        cls.voters_db[nid] = Voter(nid, password)
        return True

    @classmethod
    def authenticate(cls, nid, password):
        voter = cls.voters_db.get(nid)
        if voter and voter.password == password:
            return voter
        return None

def register_voter():
    nid = input("Enter your 10-digit NID: ")
    password = getpass.getpass("Enter a password: ")
    if Voter.add_voter(nid, password):
        print("Voter registered successfully.")
    else:
        print("Registration failed.")

def login_voter():
    nid = input("Enter your 10-digit NID: ")
    password = getpass.getpass("Enter a password: ")
    voter = Voter.authenticate(nid, password)
    if voter:
        print("Login successful.")
    else:
        print("Invalid NID or password.")
