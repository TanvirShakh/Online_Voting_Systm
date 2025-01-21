from voters import Voter

class VotingSystem:
    parties = {
        "AWAMI LEAGUE": 0,
        "BNP": 0,
        "JAMATE ISLAMI": 0,
        "GONOODHIKAR PORISHOD": 0,
        "BOISHOMMOBIRODHI CHATRO ANDOLON": 0
    }

    def vote(self):
        nid = input("Enter your 10-digit NID to vote: ")
        password = input("Enter your password to vote: ")

        # Validate NID format
        if not nid.isdigit() or len(nid) != 10:
            print("Invalid NID. Please enter a 10-digit number.")
            return

        voter = Voter.authenticate(nid, password)
        if voter:
            if voter.has_voted:
                print("You have already voted.")
                return
            print("Parties: Awami League, BNP, Jamate Islami, GonoOdhikar Porishod, Boishommobirodhi Chatro Andolon")
            choice = input("Enter the Party name you want to vote for: ").upper()
            if choice in self.parties:
                self.parties[choice] += 1
                voter.has_voted = True
                print("Vote cast successfully.")
            else:
                print("Invalid party choice.")
        else:
            print("Invalid NID or password.")

    def view_results(self):
        print("\nVoting Results:")
        for party, votes in self.parties.items():
            print(f"Party {party}: {votes} Votes.")
