import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from goalStates import winner

sign = 0  #indicates whos turn it is
max_depth = 5 #keep at 5 unless on beefy pc
previous_hashed_states = {} #store computed states for future use

global board
board = [[" " for x in range(5)] for y in range(5)]

def get_text_agent(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])

    if winner(board, "X"): #check if there's a winner or if it's a tie
        gb.destroy()
        messagebox.showinfo("Winner", "Player won the match")
        return
    elif winner(board, "O"):
        gb.destroy()
        messagebox.showinfo("Winner", "Agent won the match")
        return
    elif isfull(board):
        gb.destroy()
        messagebox.showinfo("Tie Game", "Tie Game")
        return

    if sign % 2 != 0: #if it's agent's turn it'll make the turn
        move = agent()
        if move: #disable the buttons to prevent clicking during agent move.
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_agent(move[0], move[1], gb, l1, l2)

def isfull(bd):
    for row in bd:
        if ' ' in row:
            return False
    return True

def minimax(bd, depth, alpha, beta, isMaximizing):
    board_tuple = tuple(tuple(row) for row in bd)  #convert board state to hashable type
    if board_tuple in previous_hashed_states:       #see if a state has been computed already
        return previous_hashed_states[board_tuple]

    if winner(bd, 'O'):
        return 1
    if winner(bd, 'X'):
        return -1
    if isfull(bd) or depth == 0:
        return 0
    
    if isMaximizing:
        maxEval = -float('inf')
        for i in range(5):
            for j in range(5):
                if bd[i][j] == ' ':
                    bd[i][j] = 'O'
                    eval = minimax(bd, depth - 1, alpha, beta, False)
                    bd[i][j] = ' '  #undo a move
                    maxEval = max(maxEval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        previous_hashed_states[board_tuple] = maxEval  #store the state
        return maxEval
    else:
        minEval = float('inf')
        for i in range(5):
            for j in range(5):
                if bd[i][j] == ' ':
                    bd[i][j] = 'X'
                    eval = minimax(bd, depth - 1, alpha, beta, True)
                    bd[i][j] = ' '  #undo move
                    minEval = min(minEval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        previous_hashed_states[board_tuple] = minEval  #store the state
        return minEval

def agent():
    bestScore = -float('inf') #agent is maximizer so initiate with value of -inf
    bestMove = None
    for i in range(5):
        for j in range(5):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, max_depth, -float('inf'), float('inf'), False) #alpha = -inf, beta +inf
                board[i][j] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = [i, j]
    return bestMove

def setup_style():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TButton", font=("Helvetica", 12), padding=5)
    style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), foreground="#333", background="#EEE")
    style.configure("Game.TButton", font=("Helvetica", 16, "bold"), padding=10, relief="flat")
    style.configure("TFrame", background="#FFF")
    style.configure("TLabel", background="#FFF")

def gameboard_agent(game_board, l1, l2):
    global button
    button = []
    game_frame = ttk.Frame(game_board, padding=10)
    game_frame.pack()
    for i in range(5):
        button.append([])
        for j in range(5):
            btn = ttk.Button(game_frame, text=" ", style="Game.TButton",
                             command=lambda i=i, j=j: get_text_agent(i, j, game_board, l1, l2))
            btn.grid(row=i, column=j, padx=3, pady=3)
            button[i].append(btn)
    game_board.mainloop()

def withAgent(menu):
    menu.destroy()
    game_board = tk.Tk()
    game_board.title("Tic Tac Toe")
    game_board.configure(bg="#FFF")
    
    header = ttk.Label(game_board, text="Tic Tac Toe", style="Header.TLabel")
    header.pack(pady=(10, 5))
    
    control_frame = ttk.Frame(game_board, padding=10)
    control_frame.pack()
    
    l1 = ttk.Button(control_frame, text="Player : X")
    l1.grid(row=0, column=0, padx=10)
    l2 = ttk.Button(control_frame, text="Agent : O")
    l2.state(["disabled"])
    l2.grid(row=0, column=1, padx=10)
    
    gameboard_agent(game_board, l1, l2)

def play():
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Tic Tac Toe")
    root.configure(bg="#FFF")
    
    setup_style()
    
    header = ttk.Label(root, text="--- Welcome to 5x5 Tic Tac Toe ---", style="Header.TLabel")
    header.pack(pady=20)
    
    btn_frame = ttk.Frame(root, padding=10)
    btn_frame.pack()
    
    B1 = ttk.Button(btn_frame, text="Play with the agent", command=lambda: withAgent(root))
    B1.pack(pady=10, fill="x")
    B2 = ttk.Button(btn_frame, text="Exit", command=root.quit)
    B2.pack(pady=10, fill="x")
    
    root.mainloop()

if __name__ == '__main__':
    play()
