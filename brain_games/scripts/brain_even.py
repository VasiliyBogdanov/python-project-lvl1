#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.cli import welcome_user
from brain_games.games.brain_even import even_logic


def main():
    username = welcome_user()
    engine(game_name='brain_even',
           username=username,
           game_logic=even_logic)


if __name__ == '__main__':
    main()
