"""
Player module.
"""

# Making a player class to represent each player in the game
class Player:
    """Represents a Tic-Tac-Toe player."""

    def __init__(self, name, symbol):
        """Initialize a player with a name and symbol."""
        self.name = name
        self.symbol = symbol

    def get_name(self):
        """Return the player's name."""
        return self.name
    
    def get_symbol(self):
        """Return the player's symbol."""
        return self.symbol