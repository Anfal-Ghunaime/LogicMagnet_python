from stages import Stage
from game import Game
from state import State
from piece import Piece

# init_state = [
#     [{'type': 'patch', 'is_ring': False},{'type': 'patch', 'is_ring': False},{'type': 'attract', 'is_ring': False}],
#     [{'type': 'patch', 'is_ring': True},{'type': 'patch', 'is_ring': True},{'type': 'iron', 'is_ring': False}]
# ]

# init_state = [
#     [{'type': 'patch', 'is_ring': False},{'type': 'patch', 'is_ring': False},{'type': 'repel', 'is_ring': False}],
#     [{'type': 'patch', 'is_ring': True},{'type': 'iron', 'is_ring': False},{'type': 'patch', 'is_ring': True}]
# ]

# init_state = [
#     [{'type': 'repel', 'is_ring': False},{'type': 'patch', 'is_ring': False},{'type': 'attract', 'is_ring': False}],
#     [{'type': 'patch', 'is_ring': True},{'type': 'iron', 'is_ring': True},{'type': 'patch', 'is_ring': True}]
# ]

init_state = [
                [{'type': 'attract', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'repel', 'is_ring': False}]
            ]

# stage_num = int(input("Enter stage number (From 1 to 25)"))
# stage_num = 25
# init_state, moves = Stage().getStage(stage_num)
# print(init_state)
# print(f'allowed moves: {moves}')

rows = len(init_state)
cols = len(init_state[0])
board = [[None for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        board[i][j] = Piece(i,j,init_state[i][j]['type'],init_state[i][j]['is_ring'])
stage = State(rows,cols,board, None)
print(stage)

# game = Game(stage).loop()

# game = Game(stage).DFSorBFS('DFS')

# Game = Game(stage).UCS()
# Game = Game(init_state).UCS()

Game = Game(stage).HillClimbing()

# game = Game(init_state).loop()