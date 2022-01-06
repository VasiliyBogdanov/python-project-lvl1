#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.cli import welcome_user
from brain_games.games.brain_prime import prime_logic


def main():
    username = welcome_user()
    engine(game_name='brain_prime',
           username=username,
           game_logic=prime_logic)


if __name__ == '__main__':
    main()
