from FEN import (
    getBoard,
    getExclusions,
    getRandomPosition,
    printBoard,
    setKing,
    setPieces,
    whiteDirections,
    whitePieces,
    blackDirections,
    blackPieces,
)


def generate_fens_into_file():
    with open("FENs.txt", "w") as file:
        for i in range(1000):
            exclusions = getExclusions()
            board = getBoard()
            setPieces(board, whitePieces)
            setPieces(board, blackPieces)
            setKing(board, "K", blackDirections)
            setKing(board, "k", whiteDirections)
            fen = printBoard(board)
            # getEvaluation(fen)
            # print(fen)
            file.write(fen + "\n")


if __name__ == "__main__":
    generate_fens_into_file()
