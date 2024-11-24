from copy import deepcopy
import random
import heapq

class Game:
    def __init__(self, init_state):
        self.init_state = init_state
        self.current_state = deepcopy(init_state)
        self.states = []
        self.states.append(init_state)
        self.possible_moves = []
        self.possible_moves.append(init_state)
        self.visited_states = []
        self.visited_states.append(init_state)
        self.opened = []
        heapq.heappush(self.opened, (0,self.init_state))
        self.closed = []
        # self.loop()

    def __gt__(self,state,other):
        return 
    
    def DFSorBFS(self, algo):
        # for child in self.current_state.possibleMoves():
        #     print(child)
        #     print(child.parent)
        while self.possible_moves:
            if(algo == 'BFS'):
                self.current_state = self.possible_moves.pop(0)
            else:
                self.current_state = self.possible_moves.pop()
            if self.current_state.win():
                self.visited_states.append(self.current_state)
                # for visited in self.visited_states:
                #     print(visited)
                while True:
                    print(self.current_state)
                    if self.current_state.parent is None:
                        break
                    self.current_state = self.current_state.parent
                break
            if self.current_state not in self.visited_states:
                self.visited_states.append(self.current_state)
            moves = self.current_state.possibleMoves()
            for move in moves:
               if move not in self.visited_states:
                   self.possible_moves.append(move) 

    def checkHeapq(self, element, heap):
        for heap_element in heap:
            weight, board = heap_element
            if element == board:
                return weight
            else:
                return None
            
    def delFromHeapq(self, element, heap):
        after_delete = []
        for heap_element in heap:
            weight, board = heap_element
            if element == board:
                continue
            else:
                after_delete.append((weight, board))
        heapq.heapify(after_delete)
        return after_delete


    def UCScost(self, Sstate,Fstate):
        # cost = random.randint(1,5)
        return 1

    def UCS (self):
        while self.opened:
            if not self.opened:
                print('no solution')
                break
            least_weighted = heapq.heappop(self.opened)
            weight, state = least_weighted
            if state.win():
                total_weight = 0
                while True:
                    total_weight = total_weight + state.weight
                    print(state)
                    if state.parent is None:
                        break
                    state = state.parent
                print(f"total_weight: {total_weight}")
                break
            heapq.heappush(self.closed, (weight, state))
            possible_states = state.possibleMoves()
            if possible_states:
                for possible_state in possible_states:
                    cost = weight + self.UCScost(state, possible_state)
                    possible_state.weight = self.UCScost(state, possible_state)
                    in_opened = self.checkHeapq(possible_state, self.opened)
                    in_closed = self.checkHeapq(possible_state, self.closed)
                    if in_opened is None and in_closed is None:
                        heapq.heappush(self.opened,(cost,possible_state)) 
                    else:
                        if cost < in_opened:
                            self.opened = self.delFromHeapq(possible_state, self.opened)
                            heapq.heappush(self.opened, (cost, possible_state))

    def calcHeuristic(self,state):
        heuristic = 0
        for row in state.board:
            for piece in row:
                if piece.type in ['iron','repel','attract'] and piece.is_ring == False:
                    heuristic = heuristic + 1
        return heuristic
    
    def HillClimbing(self):
        current_best = deepcopy(self.current_state)
        while(True):
            if(current_best.win()):
                while True:
                    print(current_best)
                    if current_best.parent is None:
                        break
                    current_best = current_best.parent
                break
            neighbors = current_best.possibleMoves()
            best_neighbor = neighbors[0]
            for neighbor in neighbors:
                if self.calcHeuristic(neighbor) < self.calcHeuristic(best_neighbor):
                    best_neighbor = neighbor
            if(self.calcHeuristic(best_neighbor) >= self.calcHeuristic(current_best)):
                print(current_best)
                break
            current_best = best_neighbor

    def loop(self):
        while not self.current_state.win():
            print('Which magnet you want to move next? (R for repelling magnet "purple one" and A for attraction magnet "Red one")')
            magnet = input().strip().upper()
            print("Enter next move's coordinates, x (Row num _ start from 0) then y (Column num _ from 0)")
            move_x = int(input())
            move_y = int(input())
            if (move_x<0 or move_x>self.current_state.rows):
                print('invalid input x! (out of borders)')
            elif (move_y<0 or move_y>self.current_state.cols):
                print('invalid input y! (out of borders)')
            elif magnet == 'R':
                self.moveRepel(move_x,move_y)
            elif magnet == 'A':
                self.moveAttract(move_x,move_y)
            else:
                print('inavild input magnet! (Enter R or A)')
            print(self.current_state)
        for state in self.states:
            print(state)
            

    def move(self,type,magnet_x,magnet_y,move_x,move_y):
        if type == "attract":
            self.movePiece(move_x,move_y,magnet_x,magnet_y)
            self.attract(move_x,move_y)
        elif type == "repel":
            self.movePiece(move_x,move_y,magnet_x,magnet_y)
            self.repel(move_x,move_y)
        else:
            print('invalid type')
            return 0

    def moveAttract(self, x, y):
        if self.current_state.getAttractCoord() == None:
            print('inavild choice')
            return
        attract_x, attract_y = self.current_state.getAttractCoord()
        if self.current_state.canMove(x,y):
            self.movePiece(x,y,attract_x,attract_y)
            self.attract(x,y)
            self.states.append(deepcopy(self.current_state))
        else:
            print('invalid move!')
    
    def moveRepel(self, x, y):
        if self.current_state.getRepelCoord() == None:
            print('inavild choice')
            return
        repel_x, repel_y = self.current_state.getRepelCoord()
        if self.current_state.canMove(x,y):
            self.movePiece(x,y,repel_x,repel_y)
            self.repel(x,y)
            self.states.append(deepcopy(self.current_state))
        else:
            print('invalid move!')
    
    def movePiece(self, x, y, old_x, old_y):
        self.current_state.board[x][y].type = self.current_state.board[old_x][old_y].type
        self.current_state.board[old_x][old_y].type = 'patch'

    def attract(self, x, y):  
        for piece in reversed(self.current_state.board[x][:y]):
            if piece.type in ["iron", "repel"]:
                if self.current_state.canMove(piece.x, piece.y + 1):
                    self.movePiece(piece.x, piece.y + 1, piece.x, piece.y)
        for piece in self.current_state.board[x][y + 1:]:
            if piece.type in ["iron", "repel"]:
                if self.current_state.canMove(piece.x, piece.y - 1):
                    self.movePiece(piece.x, piece.y - 1, piece.x, piece.y)
        for row in reversed(self.current_state.board[:x]):
            piece = row[y]
            if piece.type in ["iron", "repel"]:
                if self.current_state.canMove(piece.x + 1, piece.y):
                    self.movePiece(piece.x + 1, piece.y, piece.x, piece.y)
        for row in self.current_state.board[x:]:
            piece = row[y]
            if piece.type in ["iron", "repel"]:
                if self.current_state.canMove(piece.x - 1, piece.y):
                    self.movePiece(piece.x - 1, piece.y, piece.x, piece.y)

    def repel(self, x, y): 
        for piece in self.current_state.board[x][:y]:
            if piece.type in ["iron", "attract"]:
                if self.current_state.canMove(piece.x, piece.y - 1):
                    if self.canRepelRow(piece.y + 1, piece.y + 2, piece.x):
                        self.movePiece(piece.x, piece.y - 1, piece.x, piece.y)
        for piece in reversed(self.current_state.board[x][y:]):
            if piece.type in ["iron", "attract"]:
                if self.current_state.canMove(piece.x, piece.y + 1):
                    if self.canRepelRow(piece.y - 1, piece.y - 2, piece.x):
                        self.movePiece(piece.x, piece.y + 1, piece.x, piece.y)
        for row in self.current_state.board[:x]:
            piece = row[y]
            if piece.type in ["iron", "attract"]:
                if self.current_state.canMove(piece.x - 1, piece.y):
                    if self.canRepelCol(piece.x + 1 , piece.x + 2, piece.y):
                        self.movePiece(piece.x - 1, piece.y, piece.x, piece.y)
        for row in reversed(self.current_state.board[x:]):
            piece = row[y]
            if piece.type in ["iron", "attract"]:
                if self.current_state.canMove(piece.x + 1, piece.y):
                    if self.canRepelCol(piece.x-1, piece.x - 2, piece.y):
                        print(piece.x,piece.y)
                        self.movePiece(piece.x + 1, piece.y, piece.x, piece.y)

    def canRepelCol(self, x_neigh, x_next, y):
        if x_next<self.current_state.cols and x_next>0:
            if self.current_state.board[x_neigh][y].type == "patch":
                if self.current_state.board[x_next][y].type in ["iron", "attract"]:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
    
    def canRepelRow(self, y_neigh, y_next, x):
        if y_next<self.current_state.rows and y_next>0:
            if self.current_state.board[x][y_neigh].type == "patch":
                if self.current_state.board[x][y_next].type in ["iron", "attract"]:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True