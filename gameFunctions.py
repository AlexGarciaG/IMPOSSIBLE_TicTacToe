import pygame,sys
import numpy as np
pygame.init()


#Global variables
    #Board size
WIDTH = 600
HEIGHT = WIDTH 
BOARD_ROWS = 3
BOARD_COLS = 3

    #Draws
SQUARE_SIZE = WIDTH//BOARD_COLS
LINE_WIDTH = 15
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE//4
    #Colors (RGB)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BG_COLOR = (28,170,156)
LINE_COLOR = (23,145,135)
CIRCLE_COLOR = (239,231,200)
CROSS_COLOR = (66,66,66)
#FlagS
#Player 1 circle 2 cross
player = 1
#Game status
gameOver = False

#Define Screen 
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('IMPOSSIBLE TO WIN TIC TAC TOE')
programIcon = pygame.image.load('logo.png')
pygame.display.set_icon(programIcon)

screen.fill(BG_COLOR)
#board
board = np.zeros((BOARD_ROWS,BOARD_COLS))

#Draw board lines
def draw_lines():
    #1 Horizontal
    pygame.draw.line (screen, LINE_COLOR, (0,SQUARE_SIZE),(WIDTH,SQUARE_SIZE), LINE_WIDTH )
    #2 Horizontal
    pygame.draw.line (screen, LINE_COLOR, (0,SQUARE_SIZE*2),(WIDTH,SQUARE_SIZE*2), LINE_WIDTH )
    #1 Vertical
    pygame.draw.line (screen, LINE_COLOR, (SQUARE_SIZE,0),(SQUARE_SIZE,HEIGHT), LINE_WIDTH )
    #2 Vertical
    pygame.draw.line (screen, LINE_COLOR, (SQUARE_SIZE*2,0),(SQUARE_SIZE*2,HEIGHT), LINE_WIDTH )

#Place board game
def mark_square ( row,col,player):
    board[row][col] = player
#Check is available square
def available_square(board,row, col):
    return board[row][col] == 0
#check if the game is full The game end
def is_board_full ():
    for row in range (BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board [row][col]==0:
                return False
    return True
# Draw cros and circle    
def draw_figures():
    for row in range (BOARD_ROWS):
        for col in range (BOARD_COLS):
            if board [row][col]==1:
                pygame.draw.circle(screen, CIRCLE_COLOR, (int (col*SQUARE_SIZE+SQUARE_SIZE//2), int (row*SQUARE_SIZE+SQUARE_SIZE//2)), CIRCLE_RADIUS,CIRCLE_WIDTH )
            elif board [row][col]==2:
                pygame.draw.line (screen, CROSS_COLOR, (int (col*SQUARE_SIZE+SPACE), int (row*SQUARE_SIZE+SQUARE_SIZE-SPACE)),(int (col*SQUARE_SIZE+SQUARE_SIZE-SPACE), int (row*SQUARE_SIZE+SPACE)), CROSS_WIDTH )
                pygame.draw.line (screen, CROSS_COLOR, (int (col*SQUARE_SIZE+SPACE), int (row*SQUARE_SIZE+SPACE)),(int (col*SQUARE_SIZE+SQUARE_SIZE-SPACE), int (row*SQUARE_SIZE+SQUARE_SIZE-SPACE)), CROSS_WIDTH )
def check_win (player,draw,board):
    #Vertical check
    for col in range (BOARD_COLS):
        if board[0][col]==player and board[1][col]==player and board[2][col] == player:
            if draw :
                draw_vertical_winnin_line(col,player)
            return True
    #horizontal check
    for row in range (BOARD_COLS):
        if board[row][0]==player and board[row][1]==player and board[row][2] == player:
            if draw :
                draw_horizontal_winin_line(row,player)
            return True
    #asc diagonal win check
    if board[2][0]==player and board[1][1]==player and board[0][2] == player:
        if draw :
            draw_asc_diagonal(player)
        return True
    if board[0][0]==player and board[1][1]==player and board[2][2] == player:
        if draw :
            draw_des_diagonal(player)
        return True
    return False
# Draw wining lines
def draw_vertical_winnin_line(col, player):
    posX = col*SQUARE_SIZE+SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (posX,15),(posX,HEIGHT-15),15)

def draw_horizontal_winin_line(row,player):
    posY = row*SQUARE_SIZE+SQUARE_SIZE//2
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15,posY),(WIDTH-15,posY),15)

def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15,HEIGHT-15),(WIDTH-15,15),15)
def draw_des_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    pygame.draw.line(screen, color, (15,15),(WIDTH-15,HEIGHT-15),15)
#Restar game
def restar():
    screen.fill (BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0