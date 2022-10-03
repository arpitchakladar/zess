from typing import NoReturn
from game import Game

def main() -> NoReturn:
    game = Game("white")
    game.run()

if __name__ == "__main__":
    main()
