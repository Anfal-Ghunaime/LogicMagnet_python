class Piece:
    def __init__(self, x, y, type, is_ring):
        self.x = x
        self.y = y
        self.type = type
        self.is_ring = is_ring

    def __str__(self) -> str:
        if self.type == "iron":
            return '⚫️' if not self.is_ring else '🟤'
        elif self.type == "attract":
            return '🔴' if not self.is_ring else '🟠'
        elif self.type == "repel":
            return '🟣' if not self.is_ring else '🔵'
        elif self.type == "patch":
            return '🟡' if not self.is_ring else '⚪️'
        else:
            return '➖'
