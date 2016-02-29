import re

"""
Brendan Dwyer
Created on 24 Feb 2016
"""

class Seater:
    
    # this regular expression will give us the command and the rectangular bounding box
    # https://docs.python.org/2/library/re.html#re.MatchObject.group
    pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
    occupied_seats = 0
    unoccupied_seats = 1000000

    def __init__(self, size=1000):
        self.matrix = [[0 for i in xrange(size)] for i in xrange(size)]
        return
    
    def get_cmd(self, line):
        cmd, x1, y1, x2, y2 = Seater.pat.match(line).groups()
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        return cmd, x1, y1, x2, y2
    
    def seat(self, line):
        cmd, x1, y1, x2, y2 = self.get_cmd(line)
        print cmd, x1, y1, x2, y2
        if cmd == 'toggle':
            self.toggle(x1, y1, x2, y2)
        elif cmd == "occupy":
            self.occupy(x1, y1, x2, y2)
        elif cmd == 'empty':
            self.empty(x1, y1, x2, y2)
        else:
            pass
        return
    
    def occupy(self, x1, y1, x2, y2):
        for i in xrange(x1, y1 + 1):
            for j in xrange(x2, y2 + 1):
                self.matrix[i], self.matrix[j] = 1, 1

        return
    
    def empty(self, x1, y1, x2, y2):
        for i in xrange(x1, y1 + 1):
            for j in xrange(x2, y2 + 1):
                self.matrix[i], self.matrix[j] = 0, 0
        return
    
    def toggle(self, x1, y1, x2, y2):
        for i in xrange(x1, x2 + 1):
            for j in xrange(y1, y2 + 1):
                i = not i
                j = not j
        return
    
    def number_occupied(self):
        occupied = self.matrix.count(1)
        return occupied
    
if __name__ == '__main__':
    pass
