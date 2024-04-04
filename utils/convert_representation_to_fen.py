class ConvertRespresentationToFEN(object):
    def __init__(self, representation):
        self.representation = representation
        self._remove_pawns_from_backranks()

    def _is_white_backrank(self, square_num):
        return square_num in range(0, 8)

    def _is_black_backrank(self, square_num):
        return square_num in range(56, 64)

    def _is_pawn_on_backrank(self, square_num):
        if (
            (self._is_white_backrank(square_num) or self._is_black_backrank(square_num))
            and self.representation[square_num] is not None
            and "pawn" in self.representation[square_num]
        ):
            return True

    def _remove_pawn_from_backrank(self, square_num):
        if self._is_pawn_on_backrank(square_num):
            self.representation[square_num] = None

    def _remove_pawns_from_backranks(self):
        for i in range(64):
            self._remove_pawn_from_backrank(i)
