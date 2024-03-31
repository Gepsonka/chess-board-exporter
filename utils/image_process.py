import os
import cv2

from utils.constants import EDGE_WIDTH, SQUARE_SIZE

# Edge width = 15px
# Block size = 45px


class ImageProcess(object):
    def __init__(
        self, image_path, board_edge_width=EDGE_WIDTH, square_size=SQUARE_SIZE
    ):
        self._load_board_image(image_path)
        self._crop_board_image_from_the_edges(board_edge_width)
        self._load_piece_pngs()
        self._slice_board_by_blocks(square_size)

    def _load_board_image(self, path):
        self.board_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    def _load_piece_pngs(self):
        self.pieces = {}
        for piece_path in os.listdir("pieces"):
            self.pieces[piece_path.split(".")[0]] = cv2.imread(
                f"pieces/{piece_path}", cv2.IMREAD_GRAYSCALE
            )

    def _crop_board_image_from_the_edges(self, edge_width):
        image_height = self.board_image.shape[0]
        image_width = self.board_image.shape[1]

        roi = self.board_image[
            edge_width : image_height - edge_width,
            edge_width : image_width - edge_width,
        ]

        self.board_image = roi

    def _slice_board_by_blocks(self, square_size):
        self.board_squares = []
        for i in range(8):
            for j in range(8):
                square = self.board_image[
                    i * square_size : (i + 1) * square_size,
                    j * square_size : (j + 1) * square_size,
                ]
                self.board_squares.append(square)

    def _template_matching(self, square):
        pass
