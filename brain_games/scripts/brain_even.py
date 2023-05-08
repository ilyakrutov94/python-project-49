#!/usr/bin/env python3
from brain_games.even_answer import check_answer
import brain_games.scripts.brain_game


def main():
    name = brain_games.cli.welcome_user()
    check_answer(name)


if __name__ == "__main__":
    main()
