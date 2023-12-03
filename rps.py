import random

class RockPaperScissorsGame:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        while user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_choice = input("Choose rock, paper, or scissors: ").lower()
        return user_choice

    def get_computer_choice(self):
        return random.choice(['rock', 'paper', 'scissors'])

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return 'It\'s a tie!'
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            return 'You win!'
        else:
            return 'You lose!'

    def display_result(self, user_choice, computer_choice, result):
        print(f'\nYour choice: {user_choice.capitalize()}')
        print(f'Computer\'s choice: {computer_choice.capitalize()}')
        print(result)

    def play_again(self):
        return input("\nDo you want to play again? (yes/no): ").lower() == 'yes'

    def play_round(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()

        result = self.determine_winner(user_choice, computer_choice)
        self.display_result(user_choice, computer_choice, result)

        if result == 'You win!':
            self.user_score += 1
        elif result == 'You lose!':
            self.computer_score += 1

        print(f'\nScore - You: {self.user_score} | Computer: {self.computer_score}')

    def start_game(self):
        print("Welcome to Rock, Paper, Scissors Game!")

        while True:
            self.play_round()

            if not self.play_again():
                print('Thanks for playing!')
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.start_game()
