from enum import Enum

class GEN_STATE(Enum):
    SELECTED, REMOVED = 1, 0

class Gen:
    gen_state = None

    def __init__(self, state = None):
        if state == None:
            self.gen_state = GEN_STATE.REMOVED
        else:
            self.gen_state = state

    def selectGen(self):
        self.gen_state = GEN_STATE.SELECTED

    def removeGen(self):
        self.gen_state = GEN_STATE.REMOVED

    def alterGen(self):
        if (self.gen_state == GEN_STATE.SELECTED):
            self.gen_state = GEN_STATE.REMOVED
        else:
            self.gen_state = GEN_STATE.SELECTED

    def __str__(self):
        return  self.gen_state.name

    def __repr__(self):
        return  self.gen_state.name

    def __eq__(self, other):
        if isinstance(other, Gen):
            return self.state == other.state
        elif isinstance(other, GEN_STATE):
            return self.state == other
        else:
            return TypeError

    @property
    def state(self):
        return self.gen_state
