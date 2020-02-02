from rbt.game_components.player import Player
from rbt.game_components.map import Map

class GameState():
    def __init__(self):
        self.players = {}
        self.map = Map()
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
        for p in self.players.keys():
            self.players[p].setFromState(state["players"][p])

        self.map.setFromState(state['map'])

    def render(self, screen):
        self.map.render(screen)
        for p in self.players.values():
            p.render(screen)