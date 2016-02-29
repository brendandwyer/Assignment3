import re

"""
Brendan Dwyer
Created on 24 Feb 2016
"""

class Seater:
    
    # this regular expression will give us the command and the rectangular bounding box
    pat = re.compile("(.*) (\d+),(\d+) through (\d+),(\d+)")
    occupied_seats = 0
    unoccupied_seats = 1000000

    def __init__(self, size=1000):
        self.matrix = [[0 for i in xrange(size)] for i in xrange(size)]
        # declare the matrix: 1000 zeroes in the first loop, 1000 times in the second for a total of 1,000,000
        return
    
    def get_cmd(self, line):
        # Fetches the command and co-ordinates from the input file, slices them into variables.
        cmd, x1, y1, x2, y2 = Seater.pat.match(line).groups()
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        return cmd, x1, y1, x2, y2
    
    def seat(self, line):
        # Interprets the instructions from the input file and calls the relevant function with the arguments provided.
        cmd, x1, y1, x2, y2 = self.get_cmd(line)
        print cmd, x1, y1, x2, y2
        if cmd == 'toggle':
            self.toggle(x1, y1, x2, y2)
        elif cmd == "occupy":
            self.occupy(x1, y1, x2, y2)
        elif cmd == 'empty':
            self.empty(x1, y1, x2, y2)
        else:
            # the program should never reach this point unless the input file was altered.
            pass
        return
    
    def occupy(self, x1, y1, x2, y2):
        for i in xrange(x1, x2 + 1):
            for j in xrange(y1, y2 + 1):
                # nested for loop to access the square of coordinates in the matrix.
                self.matrix[i], self.matrix[j] = 1, 1
                # set elements in both axes to 1
                # (error when attempted in format 'self.matrix[i][j] = 1'

        return
    
    def empty(self, x1, y1, x2, y2):
        for i in xrange(x1, x2 + 1):
            for j in xrange(y1, y2 + 1):
                # similar functionality as above, but sets elements to empty rather than occupied.
                self.matrix[i], self.matrix[j] = 0, 0
        return
    
    def toggle(self, x1, y1, x2, y2):
        for i in xrange(x1, x2 + 1):
            for j in xrange(y1, y2 + 1):
                if self.matrix[i] == 0:
                    self.matrix[i] = 1
                else:
                    self.matrix[i] = 0
                if self.matrix[j] == 0:
                    self.matrix[j] = 1
                else:
                    self.matrix[j] = 0

                    # ugly if statements because boolean NOT didn't work as expected.
        return
    
    def number_occupied(self):
        occupied = self.matrix.count(1)
        # count the number of occurrences of '1', signifying 'occupied'.
        return occupied
    
if __name__ == '__main__':
    pass
