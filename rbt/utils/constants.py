SCREEN_RESOLUTION = (1500,1020)
PORT = 3179
MAX_PLAYERS = 1
COLOR = {
    'orange': (255,128,0),
    'blue': (0,0,255),
    'cyan': (0,255,255),
    'red': (255,0,0),
    'green': (0,255,0),
    'yellow': (255,255,0),
    'black': (0,0,0),
    'white': (255,255,255),
    'magenta': (255,0,255)
}

PLAYER_COLORS = {
    1: COLOR['orange'],
    2: COLOR['cyan']
}

MAP_WIDTH=16     # in tiles
MAP_HEIGHT=16

TILES = [
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

#TILE_PATHS = [ "rbt/game_components/T_Path.png","rbt/game_components/L_Turn.png","rbt/game_components/Vertical_Path.png","rbt/game_components/Green_Clear.png" ]

TILE_PATHS = [ 
"rbt/images/tiles/4_Way_64.png",
"rbt/images/tiles/Blank_64.png",
"rbt/images/tiles/Horizontal_64.png",
"rbt/images/tiles/L_Turn_64-1.png",
"rbt/images/tiles/L_Turn_64-2.png",
"rbt/images/tiles/L_Turn_64-3.png",
"rbt/images/tiles/L_Turn_64-4.png",
"rbt/images/tiles/T_Path_64-1.png",
"rbt/images/tiles/T_Path_64-2.png",
"rbt/images/tiles/T_Path_64-3.png",
"rbt/images/tiles/T_Path_64-4.png",
"rbt/images/tiles/Vertical_64.png"]
