"""
Prompt functions for brain_games.py.

Functions:
    welcome_user() -> None
"""
import prompt


def welcome_user():
    """Prompt user for his name and print 'Hello, {username}'."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
