#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.brain_even import even_logic, GAME_QUESTION


def main() -> None:
    engine(game_question=GAME_QUESTION,
           game_logic=even_logic)


if __name__ == '__main__':
    main()
