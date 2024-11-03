from stages import Stage
from game import Game
from state import State
from piece import Piece

init_state = [
    [{'type': 'patch', 'is_ring': False},{'type': 'attract', 'is_ring': False}],
    [{'type': 'patch', 'is_ring': False},{'type': 'patch', 'is_ring': True}]
]
stage_num = int(input("Enter stage number (From 1 to 25)"))
init_state, moves = Stage().getStage(stage_num)
print(init_state)
print(f'allowed moves: {moves}')
# rows = len(init_state)
# cols = len(init_state[0])
# board = [[None for _ in range(cols)] for _ in range(rows)]
# for i in range(rows):
#     for j in range(cols):
#         board[i][j] = Piece(i,j,init_state[i][j]['type'],init_state[i][j]['is_ring'])
# stage = State(rows,cols,board)
# print(stage)
game = Game(init_state)