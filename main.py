import os
import cv2
import numpy as np

from utils.extract_board import ExtractChessBoard
from utils.image_process import ImageProcess


extract_board = ImageProcess("screenshots/asd.png").template_match()

# image_proc = ImageProcess(
#     "data/1B1b1K2_2PP1p1b_1k1NP1pp_q2BpN1Q_P4Pp1_P3pn2_pPP1r1p1_nr2R2R w - - 0 1.png"
# )
