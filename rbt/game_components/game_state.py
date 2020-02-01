from rbt.game_components.player import Player

class GameState():
    def __init__(self):
        self.players = {}
        #TODO: Map object
        #TODO: End Game

    def getState(self):
        playerStates = {}
        for p in self.players.values():
            playerStates[p.id] = p.getState()

        return {
            "players": playerStates
        }
    
    def isOver(self):
        return False

    def update(self):
        #TODO: detect collisions n stuff
        pass

    def setGameFromState(self, state):
        # create any new player that doesn't exist
        for pState in state['players'].keys():
            if (not self.players.get(pState, False)):
                self.players[pState] = Player(pState)

        # update all the plrs
        for p in self.players.keys():
            self.players[p].setPlayerFromState(state["players"][p])

    def render(self, screen):
        for p in self.players.values():
            p.render(screen)