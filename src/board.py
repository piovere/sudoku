import numpy as np
from collections import Counter

class Board:
    def __init__(self):
        self._world = np.zeros((9, 9)).astype(np.int8)
    
    def valid(self):
        # Check rows
        for row in self.world:
            # Check for duplicates
            rdupes = [item for item, count in Counter(row).items() if count > 1]
            if not(rdupes==[0]) and not(rdupes==[]):
                # print(f"Row violation: {row}")
                return False
        for column in self.world.T:
            # Check for duplicates
            cdupes = [item for item, count in Counter(column).items() if count > 1]
            if not(cdupes==[0]) and not(cdupes==[]):
                # print(f"Column violation: {column}")
                return False
        # Somehow check for mini-squares
        for minirow in self.minisquares:
            for minisquare in minirow:
                # Check for duplicates
                ms = minisquare.ravel()
                mdupes = [item for item, count in Counter(ms).items() if count > 1]
                if not(mdupes==[0]) and not(mdupes==[]):
                    # print(f"Miniblock violation: {ms}")
                    return False
        return True
    
    @property
    def world(self):
        return self._world
    
    @property
    def minisquares(self):
        ms = np.array([
            [self._world[0:3, 0:3], self._world[0:3, 3:6], self._world[0:3, 6:9]],
            [self._world[3:6, 0:3], self._world[3:6, 3:6], self._world[3:6, 6:9]],
            [self._world[6:9, 0:3], self._world[6:9, 3:6], self._world[6:9, 6:9]],
        ])
        return ms
    
    def __repr__(self):
        return str(self._world)
    
    def set(self, value, row, column):
        tmp = np.copy(self.world)
        self._world[row, column] = value
        if not(self.valid()):
            self._world = tmp
            return False
        return True
