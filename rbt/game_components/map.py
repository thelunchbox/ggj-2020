import pygame, os, random, copy
WIDTH=10     # in tiles
HEIGHT=10
board = []
board_rects = []

class Map():

    def setBoard(self):
        self.tile_paths = [ "rbt/game_components/T_Path.png","rbt/game_components/L_Turn.png","rbt/game_components/Vertical_Path.png","rbt/game_components/Green_Clear.png" ]
        self.board       = [[0] * HEIGHT] * WIDTH
        self.board_rects = [[0] * HEIGHT] * WIDTH
        for x in range(WIDTH):
            for y in range(HEIGHT):
                #self.board[x][y] = random.choice(opts)
                self.board[x][y] = pygame.image.load(random.choice(self.tile_paths))
                #t0 = pygame.Rect(0,0,32,32).move([32*x,32*y])
                #self.board_rects[x][y] = t0
                print("here0 ",hex(id(self.board_rects[x][y])))

        for x in range(WIDTH):
            for y in range(HEIGHT):
                print("init all rects id ", hex(id(self.board_rects[x][y])))

    def __init__(self):
        self.surface = pygame.Surface((300,300))
        self.surface.fill((255,100,100))
        self.setBoard()

    def set_pos(self, pos):
        self.pos = pos

    def render(self, screen):
        print("all rects ", self.board_rects)
        for x in range(WIDTH):
            for y in range(HEIGHT):
                #print(hex(id(self.board_rects[x][y])))
                print(x,y,self.board_rects[x][y])
                #screen.blit(self.board[x][y],self.board_rects[x][y])
                screen.blit(self.board[x][y],[32*x,32*y,32,32])

