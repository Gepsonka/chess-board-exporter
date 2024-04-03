class ConvertRespresentationToFEN(object):
    def __init__(self, representation):
        self.representation = representation

    def _is_white_backrank(self, square_num):
        return square_num in range(0, 8)

    def _is_black_backrank(self, square_num):
        return square_num in range(56, 64)

    def _is_pawn_on_backrank(self, square_num):
        if (
            self._is_white_backrank(square_num) or self._is_black_backrank()
        ) and "pawn" in self.representation[square_num]:
            return True
