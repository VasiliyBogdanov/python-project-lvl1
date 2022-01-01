#!/usr/bin/env python3
"""
Main script.

Functions:
    welcome() -> None
    main()
"""
from brain_games.cli import welcome_user


def welcome():
    """Print 'Welcome to the Brain Games!' to console."""
    print('Welcome to the Brain Games!')


def main():
    """Execute main logic."""
    welcome()
    welcome_user()


if __name__ == '__main__':
    main()
