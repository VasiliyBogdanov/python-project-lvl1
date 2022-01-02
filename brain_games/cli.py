"""
Prompt functions for brain_games.py.

Functions:
    welcome() -> None
    welcome_user() -> string
"""
import prompt


def welcome():
    """Print 'Welcome to the Brain Games!' to console."""
    print('Welcome to the Brain Games!')


def welcome_user():
    """Prompt user for his name and print 'Hello, {username}'."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    return name
