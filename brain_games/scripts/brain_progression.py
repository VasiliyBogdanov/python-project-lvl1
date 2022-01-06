#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.cli import welcome_user
from brain_games.games.brain_progression import progression_logic, GAME_NAME


def main():
    username = welcome_user()
    engine(game_name=GAME_NAME,
           username=username,
           game_logic=progression_logic)


if __name__ == '__main__':
    main()
