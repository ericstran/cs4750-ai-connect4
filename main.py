from lib.Player import Player
from lib.Game import Game
from lib.Bot import Bot
from datetime import datetime


def main():
    dateTimeObj = datetime.now()
    print(dateTimeObj)
    xbot = Bot(Player.x)
    obot = Bot(Player.o)
    game = Game(1)
    print("Bot (x) vs Bot (o)")
    game.simulate(xbot, obot)

    dateTimeObj = datetime.now()
    print(dateTimeObj)


if __name__ == '__main__':
    main()
