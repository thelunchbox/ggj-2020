from rbt.game_components.hud import Hud
from rbt.game_components.player import Player
from rbt.game_components.map import Map

class GameState():
    def __init__(self):
        self.players = {}
        self.map = Map()
        self.hud = Hud()
        self.playerID = None
        #TODO: End Game

    def getState(self):
        playerStates = {}
        for p in self.players.values():
            playerStates[p.id] = p.getState()

        return {
            'players': playerStates,
            'map': self.map.getState()
        }
    
    def isOver(self):
        return False

    def update(self):
        for p in self.players.values():
            p.update()
        self.map.update()

    def setFromState(self, state):
        # create any new player that doesn't exist
        for pState in state['players'].keys():
            if (not self.players.get(pState, False)):
                self.players[pState] = Player(pState)

        # update all the plrs
        if self.playerID:
            self.players[self.playerID].setFromState(state["players"][self.playerID])

        self.map.setFromState(state['map'])

    def render(self, screen):
        self.map.render(screen)
        self.hud.render(screen)
        for p in self.players.values():
            p.render(screen)