import random

# Class to represent a player
class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
    
    def make_choice(self, choice):
        self.choice = choice

# Class to represent the game logic
class Game:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
    
    def determine_winner(self, player1, player2):
        if player1.choice == player2.choice:
            return "It's a tie!"
        
        # Dictionary to store winning conditions
        winning_conditions = {
            "rock": "scissors",  # rock beats scissors
            "scissors": "paper",  # scissors beats paper
            "paper": "rock"  # paper beats rock
        }
        
        if winning_conditions[player1.choice] == player2.choice:
            return f"{player1.name} wins!"
        else:
            return f"{player2.name} wins!"

# Class to handle game interaction and control
class GameController:
    def __init__(self):
        self.player = Player("Player")
        self.computer = Player("Computer")
        self.game = Game()
    
    def get_computer_choice(self):
        return random.choice(self.game.choices)
    
    def get_player_choice(self):
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        while choice not in self.game.choices:
            print("Invalid choice, please choose rock, paper, or scissors.")
            choice = input("Enter your choice (rock, paper, scissors): ").lower()
        return choice
    
    def play(self):
        print("Welcome to Rock, Paper, Scissors!")
        
        while True:
            # Get the player's choice
            player_choice = self.get_player_choice()
            self.player.make_choice(player_choice)
            
            # Get the computer's choice
            computer_choice = self.get_computer_choice()
            self.computer.make_choice(computer_choice)
            
            # Print choices
            print(f"{self.player.name} chose: {self.player.choice}")
            print(f"{self.computer.name} chose: {self.computer.choice}")
            
            # Determine the winner
            result = self.game.determine_winner(self.player, self.computer)
            print(result)
            
            # Ask the player if they want to play again
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != "y":
                print("Thanks for playing!")
                break

# Running the game
if __name__ == "__main__":
    controller = GameController()
    controller.play()
