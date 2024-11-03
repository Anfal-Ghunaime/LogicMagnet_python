class State:
    def __init__(self, rows,cols, board):
        self.rows = rows
        self.cols = cols
        self.board = board
        self.visited = False

    def __str__(self) -> str: 
        result = ""
        for row in self.board:
            for piece in row:
                result += str(piece)
            result += '\n'
        return result
    
    def win(self):
        done = True
        for row in self.board:
            for piece in row:
                if piece.is_ring == True and piece.type == "patch":
                    done = False
        if done == True:
            print('congratulations. you have won')
            return True
        else:
            return False
    
    def getAttractCoord(self):
        for row in self.board:
            for piece in row:
                if piece.type == "attract":
                    return piece.x, piece.y
        print('Red magnet not exist!')
        return None
    
    def getRepelCoord(self):
        for row in self.board:
            for piece in row:
                if piece.type == "repel":
                    return piece.x, piece.y
        print('Purple magnet not exist!')
        return None