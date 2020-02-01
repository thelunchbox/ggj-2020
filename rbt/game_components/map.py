import pygame, os, random, copy
WIDTH=16     # in tiles
HEIGHT=16
board = []

tiles = [
 [ 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,2 ],
 [ 1,2,3,0, 2,0,1,2, 1,3,0,1, 2,1,3,2 ],
 [ 2,3,0,2, 0,2,2,3, 3,3,2,2, 3,3,3,2 ],
 [ 2,2,1,2, 2,1,2,2, 2,3,1,2, 2,2,3,2 ],

 [ 3,1,0,2, 0,1,2,2, 3,3,1,2, 2,3,3,2 ],
 [ 1,3,1,2, 0,3,2,2, 3,3,3,3, 0,0,0,0 ],
 [ 2,3,0,2, 0,1,2,0, 1,3,1,3, 1,3,0,1 ],
 [ 0,3,0,2, 0,0,2,3, 1,2,1,2, 3,3,2,2 ],

 [ 2,3,0,2, 0,1,2,1, 0,2,0,2, 2,3,1,2 ],
 [ 2,3,0,2, 0,3,2,3, 1,3,1,3, 3,3,1,2 ],
 [ 0,0,0,0, 0,0,0,0, 0,0,0,0, 0,0,0,2 ],
 [ 1,2,3,0, 2,0,1,2, 1,3,0,1, 2,1,3,2 ],

 [ 2,3,0,2, 0,2,2,3, 3,3,2,2, 3,3,3,2 ],
 [ 2,2,1,2, 2,1,2,2, 2,3,1,2, 2,2,3,2 ],
 [ 3,1,0,2, 0,1,2,2, 3,3,1,2, 2,3,3,2 ],
 [ 1,3,1,2, 0,3,2,2, 3,3,3,3, 0,0,0,0 ]
]

TILE_PATHS = [ "rbt/game_components/T_Path.png","rbt/game_components/L_Turn.png","rbt/game_components/Vertical_Path.png","rbt/game_components/Green_Clear.png" ]
TILE_SURFACES = []
for file in TILE_PATHS:
    TILE_SURFACES.append(pygame.image.load(file))


class Map():
    def __init__(self):
        #self.surface = pygame.Surface((300,300))
        #self.surface.fill((255,100,100))
        self.setBoard()

    def setBoard(self):
        self.board       = []
        for x in range(WIDTH):
            self.board.append([])
            for y in range(HEIGHT):
                self.board[x].append(TILE_SURFACES[tiles[x][y]])


    def render(self, screen):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                screen.blit(self.board[x][y],(64*x,64*y,64,64))

