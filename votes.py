from voters import Voter

class VotingSystem:
    parties = {"AWAMI LEAGUE": 0, "BNP": 0, "JAMATE ISLAMI": 0}

    def vote(self):
        username = input("Enter your username to vote: ")
        password = input("Enter your password to vote: ")
        voter = Voter.authenticate(username, password)
        if voter:
            if voter.has_voted:
                print("You have already voted.")
                return
            print("Parties: Awami League, BNP, Jamate Islami")
            choice = input("Enter the Party name you want to vote for: ").upper()
            if choice in self.parties:
                self.parties[choice] += 1
                voter.has_voted = True
                print("Vote cast successfully.")
            else:
                print("Invalid party choice.")
        else:
            print("Invalid username or password")

    def view_results(self):
        print("\nVoting Results:")
        for party, votes in self.parties.items():
            print(f"Party {party}: {votes} Votes.")
