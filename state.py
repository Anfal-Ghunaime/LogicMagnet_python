from copy import deepcopy
from game import Game
class State:
    def __init__(self, rows,cols, board, parent):
        self.rows = rows
        self.cols = cols
        self.board = board
        self.parent = parent
        self.weight = 0

    def __gt__(self,other):
        return

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
    
    def canMove(self, x, y):
        if x < 0:
            return False
        elif x >= self.rows:
            return False
        elif y < 0:
            return False 
        elif y >= self.cols:
            return False 
        elif self.board[x][y].type == 'patch':
            return True
        else:
            return False
    
    def possibleMoves(self):
        attract = True
        repel = True
        if self.getAttractCoord() == None:
            attract = False
        if self.getRepelCoord() == None:
            repel = False
        moves = []
        #attract magnet moves
        if (attract == True):
            attract_x,attract_y = self.getAttractCoord()
            for i in range (self.rows):
                for j in range(self.cols):
                    if self.canMove(i,j):
                        current_move = deepcopy(self)
                        parent = deepcopy(self)
                        current_move.board[i][j].type = current_move.board[attract_x][attract_y].type
                        current_move.board[attract_x][attract_y].type = 'patch'
                        current_move.parent = parent
                        for piece in reversed(current_move.board[i][:j]):
                            if piece.type in ["iron", "repel"]:
                                if current_move.canMove(piece.x, piece.y + 1):
                                    current_move.movePiece(piece.x, piece.y + 1, piece.x, piece.y)
                        for piece in current_move.board[i][j + 1:]:
                            if piece.type in ["iron", "repel"]:
                                if current_move.canMove(piece.x, piece.y - 1):
                                    current_move.movePiece(piece.x, piece.y - 1, piece.x, piece.y)
                        for row in reversed(current_move.board[:i]):
                            piece = row[j]
                            if piece.type in ["iron", "repel"]:
                                if current_move.canMove(piece.x + 1, piece.y):
                                    current_move.movePiece(piece.x + 1, piece.y, piece.x, piece.y)
                        for row in current_move.board[i:]:
                            piece = row[j]
                            if piece.type in ["iron", "repel"]:
                                if current_move.canMove(piece.x - 1, piece.y):
                                    current_move.movePiece(piece.x - 1, piece.y, piece.x, piece.y)
                        moves.append(deepcopy(current_move))
        #repel magnet move
        if (repel == True):
            repel_x, repel_y = self.getRepelCoord()
            for i in range (self.rows):
                for j in range(self.cols):
                    if self.canMove(i,j):
                        current_move = deepcopy(self)
                        current_move.board[i][j].type = current_move.board[repel_x][repel_y].type
                        current_move.board[repel_x][repel_y].type = 'patch'
                        current_move.parent = parent
                        for piece in current_move.board[i][:j]:
                            if piece.type in ["iron", "attract"]:
                                if current_move.canMove(piece.x, piece.y - 1):
                                    if current_move.canRepelRow(piece.y + 1, piece.y + 2, piece.x):
                                        current_move.movePiece(piece.x, piece.y - 1, piece.x, piece.y)
                        for piece in reversed(current_move.board[i][j:]):
                            if piece.type in ["iron", "attract"]:
                                if current_move.canMove(piece.x, piece.y + 1):
                                    if current_move.canRepelRow(piece.y - 1, piece.y - 2, piece.x):
                                        current_move.movePiece(piece.x, piece.y + 1, piece.x, piece.y)
                        for row in current_move.board[:i]:
                            piece = row[j]
                            if piece.type in ["iron", "attract"]:
                                if current_move.canMove(piece.x - 1, piece.y):
                                    if current_move.canRepelCol(piece.x + 1 , piece.x + 2, piece.y):
                                        current_move.movePiece(piece.x - 1, piece.y, piece.x, piece.y)
                        for row in reversed(current_move.board[i:]):
                            piece = row[j]
                            if piece.type in ["iron", "attract"]:
                                if current_move.canMove(piece.x + 1, piece.y):
                                    if current_move.canRepelCol(piece.x-1, piece.x - 2, piece.y):
                                        current_move.movePiece(piece.x + 1, piece.y, piece.x, piece.y)
                        moves.append(deepcopy(current_move))
        #possible moves list
        return moves
    
    def canRepelCol(self, x_neigh, x_next, y):
        if self.board[x_neigh][y].type == "patch":
            if x_next<self.cols and x_next>0:
                if self.board[x_next][y].type in ["iron", "attract"]:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
    
    def canRepelRow(self, y_neigh, y_next, x):
        if self.board[x][y_neigh].type == "patch":
            if y_next<self.rows and y_next>0:
                if self.board[x][y_next].type in ["iron", "attract"]:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
    
    def movePiece(self, x, y, old_x, old_y):
        self.board[x][y].type = self.board[old_x][old_y].type
        self.board[old_x][old_y].type = 'patch'