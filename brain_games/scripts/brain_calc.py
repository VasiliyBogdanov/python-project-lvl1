#!/usr/bin/env python3

from brain_games.engine import engine
from brain_games.games.brain_calc import calc_logic, GAME_QUESTION


def main():
    engine(game_question=GAME_QUESTION,
           game_logic=calc_logic)


if __name__ == '__main__':
    main()
