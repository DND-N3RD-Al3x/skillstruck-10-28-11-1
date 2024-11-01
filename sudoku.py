import pygame
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 540, 600
GRID_SIZE = 9
CELL_SIZE = WIDTH // GRID_SIZE
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
FONT = pygame.font.Font(None, 36)

# Example Sudoku puzzle (0 represents an empty cell)
SUDOKU_BOARD = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 9, 0, 0, 0, 0, 4, 0],
    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],
    [0, 3, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 7, 3, 0, 0, 0, 9, 1],
    [0, 0, 0, 7, 0, 2, 0, 3, 0]
]

# Helper functions
def draw_grid():
    """Draw the Sudoku grid lines on the screen."""
    for i in range(GRID_SIZE + 1):
        line_thickness = 4 if i % 3 == 0 else 1
        pygame.draw.line(SCREEN, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT - 60), line_thickness)
        pygame.draw.line(SCREEN, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), line_thickness)

def draw_numbers(board):
    """Draw the numbers on the Sudoku board."""
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            num = board[row][col]
            if num != 0:
                text = FONT.render(str(num), True, BLACK)
                SCREEN.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 3))

def is_valid(board, num, pos):
    """Check if the number is valid in the current board state."""
    row, col = pos

    # Check row
    for i in range(GRID_SIZE):
        if board[row][i] == num and col != i:
            return False

    # Check column
    for i in range(GRID_SIZE):
        if board[i][col] == num and row != i:
            return False

    # Check 3x3 box
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def find_empty(board):
    """Find an empty cell in the board."""
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def redraw_window(board):
    """Redraw the game window."""
    SCREEN.fill(WHITE)
    draw_grid()
    draw_numbers(board)

def main():
    key = None
    selected = None
    board = [row[:] for row in SUDOKU_BOARD]  # Create a copy of the initial board
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get mouse position
                x, y = pygame.mouse.get_pos()
                if y < HEIGHT - 60:  # Only allow clicking within the grid
                    row = y // CELL_SIZE
                    col = x // CELL_SIZE
                    selected = (row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    key = 0

                if event.key == pygame.K_RETURN:
                    if selected and key is not None:
                        row, col = selected
                        if SUDOKU_BOARD[row][col] == 0:
                            if is_valid(board, key, (row, col)):
                                board[row][col] = key
                            key = None

        redraw_window(board)

        if selected and key is not None:
            row, col = selected
            text = FONT.render(str(key), True, GRAY)
            SCREEN.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 3))

        pygame.display.update()

    pygame.quit()

main()
