import argparse
from utils.extract_board import ExtractChessBoard
from utils.image_process import ImageProcess

parser = argparse.ArgumentParser()
parser.add_argument("--path", type=str, help="Path to the screenshot")
parser.add_argument(
    "--show-process", type=bool, help="Show the process of extracting the chess board"
)

args = parser.parse_args()

if args.path is None:
    path = "screenshots/asd.png"
else:
    path = args.path

if args.show_process is None:
    show_process = False
else:
    show_process = args.show_process

proc = ImageProcess(
    path,
    show_process=show_process,
).template_match()
