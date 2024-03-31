from chess import svg
import chess
import cairosvg

from utils.constants import PIECE_SIGNS


def export_chess_pieces():
    for index, (piece_sign, designation) in enumerate(PIECE_SIGNS.items()):
        piece_svg = svg.piece(chess.Piece.from_symbol(piece_sign))
        print(piece_svg)
        cairosvg.svg2png(
            bytestring=piece_svg, write_to=f"pieces/{designation}.png", output_height=45
        )


if __name__ == "__main__":
    export_chess_pieces()
