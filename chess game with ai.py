import pygame
import chess
import chess.engine

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 480, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game with AI")

# Load chess board images
board_img = pygame.image.load("chessboard.png")  # Add chessboard image
piece_imgs = {piece: pygame.image.load(f"pieces/{piece}.png") for piece in ["wp", "bp", "wn", "bn", "wb", "bb", "wr", "br", "wq", "bq", "wk", "bk"]}  # Add pieces images

# Chess engine setup
engine = chess.engine.SimpleEngine.popen_uci("stockfish")  # Download Stockfish engine for AI

# Chess board setup
board = chess.Board()

running = True
selected_square = None

while running:
    screen.blit(board_img, (0, 0))  # Draw board

    # Draw pieces
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            img = piece_imgs[piece.symbol().lower() + ("w" if piece.color else "b")]
            row, col = divmod(square, 8)
            screen.blit(img, (col * 60, row * 60))

    pygame.display.update()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col, row = x // 60, y // 60
            square = chess.square(col, row)

            if selected_square is None and board.piece_at(square):
                selected_square = square  # Select a piece
            elif selected_square is not None:
                move = chess.Move(selected_square, square)
                if move in board.legal_moves:
                    board.push(move)  # Move piece
                    result = engine.play(board, chess.engine.Limit(time=0.5))  # AI makes a move
                    board.push(result.move)

                selected_square = None  # Reset selection

pygame.quit()
engine.quit()