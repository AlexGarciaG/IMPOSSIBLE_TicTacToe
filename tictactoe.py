import gameFunctions as gF
import numpy as np
import random
import sys

AI = 1
PLAYER = 2
MINIMAXSCORES= {
  'AI': 100,
  'PLAYER': -100,
  'TIE': 0
}

def aiMove():
    depth=0
    bestScore = -3
    bestMoves = np.array([[2,2]])
    for row in range(gF.BOARD_ROWS):
        for col in range(gF.BOARD_COLS):
            if gF.available_square( gF.board,row,col):
                gF.board[row][col] = AI
                score = minimax(np.copy(gF.board), False,depth+1)
                gF.board[row][col] = 0
                if (score > bestScore):
                    bestScore = score
                    bestMoves = np.array([[row,col]])
                elif (score == bestScore):
                    bestMoves = np.append(bestMoves,[[row,col]],axis = 0)
    
    totalOfBestMoves = len(bestMoves)
    posibleBestMove = random.randint(0, totalOfBestMoves-1)
    iaMove = bestMoves[posibleBestMove]
    gF.board[iaMove[0]][iaMove[1]] = AI
    return
    

def chekEndGame (board):
    if (gF.check_win(AI,False,board)):
        return 'AI'
    elif(gF.check_win(PLAYER,False,board)):
        return 'PLAYER'
    elif(gF.is_board_full()):
        return 'TIE'
    else:
        return ''

def minimax (board,ai,depth):

    #Check end of the game
    result = chekEndGame (board)
    if (result != ''):
        return MINIMAXSCORES[result]
    
    #calcule the best move for the ia 
    if (ai):
        bestScore = -200
        #check all boards moves
        for row in range(gF.BOARD_ROWS):
            for col in range(gF.BOARD_COLS):
                #Check if is posible to place 
                if gF.available_square(board,row,col):
                    #Place Ia
                    board[row][col] = AI
                    #Go depther
                    score = minimax(np.copy(board), False,depth+1)
                    board[row][col] = 0
                    if score > bestScore:
                        bestScore = score
        return bestScore/depth
    #calcule the best move for the player     
    else:
        bestScore = 200
        #check all boards moves
        for row in range(gF.BOARD_ROWS):
            for col in range(gF.BOARD_COLS):
                #Check if is posible to place 
                if gF.available_square(board,row,col):
                    #Place player
                    board[row][col] = PLAYER
                    #Go depther
                    score = minimax(board, True,depth+1)
                    board[row][col] = 0
                    if score<bestScore:
                        bestScore = score
        return bestScore/depth

#Draw initial map
gF.draw_lines()
gF.pygame.display.update()



#mainlop
while True:
    if PLAYER == gF.player:
        for event in gF.pygame.event.get():
            #Exit the game
            if event.type == gF.pygame.QUIT:
                gF.sys.exit()
            #Get mouse CLICK
            if event.type == gF.pygame.MOUSEBUTTONDOWN and not gF.gameOver:
                if event.button == 1:
                    #Get x and Y cordenates (maxValue == Board Size )
                    mouseX = event.pos[0]#x
                    mouseY = event.pos[1]#y
                    #Get board place
                    clicked_row = int(mouseY //gF.SQUARE_SIZE)
                    clicked_col = int(mouseX //gF.SQUARE_SIZE)
                    #Place in board
                    if gF.available_square(gF.board,clicked_row,clicked_col):
                        gF.mark_square(clicked_row,clicked_col,gF.player)
                        gF.player = AI
                        if gF.check_win(PLAYER,True,gF.board):
                            gF.gameOver = True
                        if gF.check_win(AI,True,gF.board):
                            gF.gameOver = True   
                        if gF.is_board_full():
                            gF.gameOver = True
                gF.pygame.event.clear()
            if event.type == gF.pygame.KEYDOWN:
                
                if event.key == gF.pygame.K_r:
                    
                    gF.restar()
                    gF.player = 1
                    gF.gameOver = False
                    gF.draw_figures()
                    gF.pygame.display.update()
                    gF.pygame.event.clear()

            #Draw basic board
    elif AI == gF.player and not gF.gameOver:
        gF.pygame.event.clear()
        aiMove()
        if gF.check_win(PLAYER,True,gF.board):
            gF.gameOver = True
        if gF.check_win(AI,True,gF.board):
            gF.gameOver = True   
        if gF.is_board_full():
            gF.gameOver = True
        gF.player = PLAYER
        
    #Check end game conditions
    gF.pygame.event.clear()
    gF.draw_figures()
    gF.pygame.display.update()



                



