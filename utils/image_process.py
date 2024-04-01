import os
import cv2
import numpy as np

from utils.display_image import display_image
from utils.constants import EDGE_WIDTH, SQUARE_SIZE
from utils.extract_board import ExtractChessBoard

# Edge width = 15px
# Block size = 45px


class ImageProcess(object):
    TEMPLATE_SCALES = [1]

    def __init__(self, image_path):
        self._load_board_image(image_path)
        self._extract_board()
        self._slice_board_by_blocks()
        self._load_piece_pngs()

    def _load_board_image(self, path):
        self.board_image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        self.board_image = cv2.threshold(self.board_image, 120, 255, cv2.THRESH_BINARY)[
            1
        ]

    def convert_alpha_to_white(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

        return image

    def _load_piece_pngs(self):
        self.pieces = {}
        for piece_path in os.listdir("pieces"):
            template = cv2.imread(f"pieces/{piece_path}", cv2.IMREAD_UNCHANGED)

            # Convert alpha to white
            template_mask = template[:, :, 3] == 0

            template[template_mask] = [255, 255, 255, 255]

            template = cv2.cvtColor(template, cv2.COLOR_BGRA2GRAY)

            template = cv2.resize(
                template,
                (self.square_size, self.square_size),
            )

            mask = cv2.inRange(template, 254, 255)
            mask = cv2.bitwise_not(mask)

            cnt, _ = cv2.findContours(
                mask,
                cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE,
            )

            if cnt:
                cnt = max(cnt, key=cv2.contourArea)
                x, y, w, h = cv2.boundingRect(cnt)

                template = template[y : y + h, x : x + w]

            self.pieces[piece_path.split(".")[0]] = {
                "template": template,
                "mask": None,
            }

    def _extract_board(self):
        self.board_image = ExtractChessBoard(image_obj=self.board_image).extract_board()

    def _slice_board_by_blocks(self):
        self.square_size = self.board_image.shape[0] // 8
        print("square size: ", self.square_size)
        self.board_squares = []
        for i in range(8):
            for j in range(8):
                square = self.board_image[
                    i * self.square_size : (i + 1) * self.square_size,
                    j * self.square_size : (j + 1) * self.square_size,
                ]
                self.board_squares.append(square)

    def template_match(self):
        self.board_representation = []
        for i in range(64):
            square = self.board_squares[i]
            piece = self._template_match_square(square)
            self.board_representation.append(piece)

        print(self.board_representation)

    def _template_match_square(self, square):
        biggest_score = {"piece": None, "score": 0}
        for piece_name, piece_obj in self.pieces.items():
            res = cv2.matchTemplate(
                square,
                piece_obj["template"],
                cv2.TM_CCORR_NORMED,
                # mask=piece_obj["mask"],
            )
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            bottom_right = (
                max_loc[0] + piece_obj["template"].shape[1],
                max_loc[1] + piece_obj["template"].shape[0],
            )

            # display_image(square, "square")
            # display_image(piece_obj["template"], "template")

            if max_val > 0.905 and max_val > biggest_score["score"]:
                biggest_score["piece"] = piece_name
                biggest_score["score"] = max_val

        return biggest_score["piece"]
