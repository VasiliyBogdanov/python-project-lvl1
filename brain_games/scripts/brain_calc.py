#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.brain_calc import calc_game


def main():
    username = welcome_user()
    calc_game(username)


if __name__ == '__main__':
    main()
