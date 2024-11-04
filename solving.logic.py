"""
cube layout:

    UUU
    UUU
    UUU
LLL FFF RRR BBB
LLL FFF RRR BBB
LLL FFF RRR BBB
    DDD
    DDD
    DDD

each face:

0 1 2
3 4 5
6 7 8

"""

class piece:
    
    def __init__(self, face, pos, colors):

        """
        face: a letter in ['F', 'U', 'D', 'L', 'R', 'B'] that determines the face in which the piece lies
        pos: an integer between [0, 8] that determines its position in the face
        colors: a tuple (x, y, z) where each of x, y, z is in ['W', 'R', 'B', 'O', 'G', 'Y'] that determines the color of the piece in that vector
        """

        self.face = face
        self.pos = pos
        self.colors = colors

        if colors.count(None) == 2:
            self.type = 'FACE'
        elif colors.count(None) == 1:
            self.type = 'EDGE'
        else:
            self.type = 'CORNER'

class cube:

    def __init__(self):
        