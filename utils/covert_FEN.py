import unittest


def convert_FEN(FEN: str):
    """
    Converting FEN into a 1 dimension representation of the board
    which is a list of 64 elements. Each element is a string
    Capital letters represent white pieces and small letters represent black pieces.
    r - rook
    n - knight
    b - bishop
    q - queen
    k - king
    p - pawn
    - - empty square
    """
    representation = []
    for char in FEN:
        if char == "/" or char == "_":
            continue
        if char.isalpha():
            representation.append(char)
        elif char.isdigit():
            for i in range(int(char)):
                representation.append("-")
        if char == " ":
            break

    return representation
