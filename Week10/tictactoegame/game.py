"""
Tic-Tac-Toe Game Module.
"""

from player import Player

# Main game class to handle game logic and flow
class TicTacToe:
    """Main Tic-Tac-Toe game class."""

    def __init__(self):
        """Create board and players."""
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

        # Initialize two players with their names and symbols
        self.player1 = Player("Player 1", "X")
        self.player2 = Player("Player 2", "O")

        self.current_player = self.player1

    # Method to display the current state of the board
    def display_board(self):
        """Display board."""
        print()

        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row, col):
        """Place symbol on board."""

        if self.board[row][col] == " ":
            self.board[row][col] = (
                self.current_player.get_symbol()
            )
            return True

        return False

    def switch_player(self):
        """Switch player turn."""

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def check_winner(self):
        """Check winning conditions."""

        symbol = self.current_player.get_symbol()

        # Rows
        for row in self.board:
            if row.count(symbol) == 3:
                return True

        # Columns
        for col in range(3):
            if all(
                self.board[row][col] == symbol
                for row in range(3)
            ):
                return True

        # Diagonal
        if all(
            self.board[i][i] == symbol
            for i in range(3)
        ):
            return True

        # Reverse diagonal
        if all(
            self.board[i][2 - i] == symbol
            for i in range(3)
        ):
            return True

        return False

    def check_draw(self):
        """Check draw condition."""

        for row in self.board:
            if " " in row:
                return False

        return True

    def start_game(self):
        """Start game loop."""

        while True:
            
            # Display the current board state
            self.display_board()

            # Prompt the current player for their move
            print(
                f"\n{self.current_player.get_name()}'s turn "
                f"({self.current_player.get_symbol()})"
            )

            # Get user input for row and column
            try:
                row = int(input("Row (0-2): "))
                col = int(input("Column (0-2): "))

                if row not in range(3) or col not in range(3):
                    print("Invalid position.")
                    continue

            except ValueError:
                print("Numbers only.")
                continue

            if not self.make_move(row, col):
                print("Position already taken.")
                continue

            if self.check_winner():
                self.display_board()

                print(
                    f"\n{self.current_player.get_name()} Wins!"
                )
                break

            if self.check_draw():
                self.display_board()

                print("\nGame Draw!")
                break

            self.switch_player()