from state import State
from piece import Piece
class Stage:
    def __init__(self):
        self.stages = {
            1: ([
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],5),
            2: ([
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}]
            ],5),
            3: ([
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],5),
            4: ([
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],2),
            5: ([
                [{'type': 'patch', 'is_ring': True}, {'type': 'filler', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': True}, {'type': 'filler', 'is_ring': False}, {'type': 'iron', 'is_ring': True}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],2),
            6: ([
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],2),
            7: ([
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': False}, {'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'iron', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'filler', 'is_ring': False}]
            ],2),
            8: ([
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],2),
            9: ([
                [{'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],2),
            10: ([
                [{'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'iron', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}]
            ],2),
            11: ([
                [{'type': 'iron', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'attract', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],1),
            12: ([
                [{'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'attract', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],1),
            13: ([
                [{'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'iron', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'attract', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],2),
            14: ([
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'attract', 'is_ring': False}]
            ],2),
            15: ([
                [{'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'attract', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],2),
            16: ([
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'attract', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'repel', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}]
            ],3),
            17: ([
                [{'type': 'attract', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'repel', 'is_ring': False}]
            ],2),
            18: ([
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': True}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'attract', 'is_ring': False}, {'type': 'repel', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],2),
            19: ([
                [{'type': 'filler', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'repel', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'attract', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],4),
            20: ([
                [{'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'repel', 'is_ring': False}, {'type': 'attract', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],2),
            21: ([
                [{'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'repel', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'attract', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],2),
            22: ([
                [{'type': 'repel', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'filler', 'is_ring': False}, {'type': 'iron', 'is_ring': True}, {'type': 'iron', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'attract', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],3),
            23: ([
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}],
                [{'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'attract', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'repel', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],3),
            24: ([
                [{'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'repel', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}],
                [{'type': 'attract', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}],
                [{'type': 'filler', 'is_ring': False}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],3),
            25: ([
                [{'type': 'iron', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'attract', 'is_ring': True}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'patch', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'iron', 'is_ring': False}, {'type': 'patch', 'is_ring': False}, {'type': 'filler', 'is_ring': False}],
                [{'type': 'repel', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'patch', 'is_ring': True}, {'type': 'iron', 'is_ring': False}, {'type': 'filler', 'is_ring': False}]
            ],3)
        }
    
    def getStage(self, stage_num):
        choosed_stage, moves = self.stages[stage_num]
        rows = len(choosed_stage)
        cols = len(choosed_stage[0])
        board = [[None for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                board[i][j] = Piece(i,j,choosed_stage[i][j]['type'],choosed_stage[i][j]['is_ring'])
        stage = State(rows,cols,board)
        return stage, moves