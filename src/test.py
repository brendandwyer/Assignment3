matrix =

def occupy(self, x1, y1, x2, y2):
    for i in xrange(x1, y1):
        for j in xrange(x2, y2):
            if self.matrix[j] == 0:
                self.matrix[j] = 1

