from rbt.game_components.player import Player

class GameState():
    def __init__(self):
        # list of players (max=2 for now)
        self.players = {}
        #TODO: Map object
        #TODO: End Game

    def getState(self):
        playerStates = {}
        for p in self.players.values():
            playerStates[str(p.id)] = p.getState()

        return {
            "players": playerStates
        }
    
    def isOver(self):
        return False

    def update(self):
        pass

    def setGameFromState(self, state):
        for pState in state['players'].keys():
            if (not self.players.get(pState.id, False)):
                self.players[pState.id] = Player(pState.id)

        for p in self.players.keys():
            self.players[p].setPlayerFromState(state["players"][p])

    def render(self, screen):
        for p in self.players.values():
            p.render(screen)