#!/usr/bin/env python3
"""
Main script.

Functions:
    welcome() -> None
    main()
"""
from brain_games.cli import welcome, welcome_user


def main():
    """Execute main logic."""
    welcome()
    welcome_user()


if __name__ == '__main__':
    main()
