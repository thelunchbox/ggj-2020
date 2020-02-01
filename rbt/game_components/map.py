import pygame, os, random
WIDTH=3 # in tiles
HEIGHT=3

class Map():
    def __init__(self):
        print(os.getcwd())
        self.tpath = pygame.image.load("rbt/game_components/T_Path.png")
        self.lpath = pygame.image.load("rbt/game_components/L_Turn.png")
        self.vpath = pygame.image.load("rbt/game_components/Vertical_Path.png")
        self.green = pygame.image.load("rbt/game_components/Green_Clear.png")
        opts = [ self.tpath,self.lpath,self.vpath,self.green ]

        self.board       = [[0] * HEIGHT] * WIDTH
        self.board_rects = [[0] * HEIGHT] * WIDTH
        for x in range(WIDTH):
            for y in range(HEIGHT):
                self.board[x][y] = random.choice(opts)
                print("board: ", self.board[x][y])
                self.board_rects[x][y] = self.board[x][y].get_rect()
                self.board_rects[x][y] = self.board_rects[x][y].move([32 * x, 32 * y])
                #self.board_rects[x][y] = self.board_rects[x][y].move([x, y])
                print(x,y)


        self.surface = pygame.Surface((300,300))
        self.surface.fill((255,100,100))
    def set_pos(self, pos):
        self.pos = pos
    def render(self, screen):
        #screen.blit(self.tpath,self.tpath_rect)
        #screen.blit(self.lpath,self.lpath_rect)
        for x in range(WIDTH):
            for y in range(HEIGHT):
                #print(self.board_rects[x][y])
                screen.blit(self.board[x][y],self.board_rects[x][y])

