# Online_Voting_Systm


This project is a **Python-based Online Voting System** built using a command-line interface. It allows users to register, log in, and vote for their preferred political party. Administrators can view the results, and users can vote only once to ensure fairness.

## Features

- **Secure User Registration and Login:**
  - Passwords are securely handled.
  - Users cannot register with an already existing username.
- **One Person, One Vote:**
  - Each user can vote only once.
  - Votes are tied to authenticated users to prevent multiple votes.
- **Dynamic Party Selection:**
  - Users can vote for one of the listed parties.
- **Voting Results:**
  - Real-time voting results can be viewed by administrators.
- **Easy to Use:**
  - Simple, command-line-based user interface for straightforward interaction.

## Political Parties and Candidates

- **Awami League** (`Nouka`) - Sheikh Hasina
- **BNP** (`Dhaner Shish`) - Khaleda Zia
- **Jamaat-e-Islami** (`Daripalla`) - Dr. Shoriful Islam
- **Gonoodhikar Parishad** (`Pen`) - VP Noor

## How It Works

1. **Register a Voter:**
   Users can create an account by providing a unique username and password.

2. **Log In:**
   Existing users can log in using their credentials.

3. **Cast a Vote:**
   After logging in, users can select a party to vote for.

4. **View Results:**
   Real-time vote counts for all parties can be viewed.

5. **Exit:**
   Users can exit the system after completing their actions.

## File Structure

- **`voters.py`:** Handles user registration, authentication, and user data management.
- **`votes.py`:** Contains the voting system logic, including voting and result calculation.
- **`main.py`:** Entry point for the system, providing a menu-driven interface for interaction.

## Requirements

- Python 3.x installed on your system.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/online-voting-system.git
   cd online-voting-system
   ```

2. Run the program:
   ```bash
   python main.py
   ```

3. Follow the menu options to register, log in, vote, view results, or exit.



Feel free to modify the content to suit your preferences or add any additional features your project includes!
