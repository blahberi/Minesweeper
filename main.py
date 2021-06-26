from Minesweeper.Game import Game
minesweeper = Game((8, 8), 10)
while True:
    print(minesweeper)
    location_x = int(input('x: '))
    location_y = int(input('y: '))
    minesweeper.select((location_x, location_y))
    if minesweeper.GAME_OVER:
        print('GAME OVER')
        break