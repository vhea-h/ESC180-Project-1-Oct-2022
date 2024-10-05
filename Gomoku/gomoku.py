"""
Gomoku starter code author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  

Student Modifications Done by: Vhea He
Student Number: 1009525202
UTORid: hevhea
"""

def is_empty(board):
    for y in board:
        for x in y:
            if x != " ":
                return False
    return True

#HELPER FUNCTION
#Determines whether a given index is a valid location on the board
def is_valid_space(y, x, board):
    if y < 0 or y >= len(board):
        return False
    if x < 0 or x >= len(board[0]):
        return False
    return True

#HELPER FUNCTION
#Determines whether a given position would qualify as an "open" or "closed" end
def is_open_end(y, x, board):
    if is_valid_space(y, x, board) == False or board[y][x] != " ":
        return False
    return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    num_open_ends = 0 
    
    #Check space after sequence ending
    if is_open_end(y_end + d_y, x_end + d_x, board):
        num_open_ends += 1
    #Check space before sequence ending
    if is_open_end(y_end - d_y*length, x_end - d_x*length, board):
        num_open_ends += 1
    
    #Return type of bound based on number of open ends
    if num_open_ends == 2:
        return "OPEN"
    elif num_open_ends == 1:
        return "SEMIOPEN"
    elif num_open_ends == 0:
        return "CLOSED"
    else:
        print("UNEXPECTED OPEN ENDS ERROR")
        return None

#HELPER FUNCTION
#Get the length of the whole "row" you will be checking
def get_row_len(board, y_start, x_start, d_y, d_x):
    #hori and verti is 8
    if d_y == 0 or d_x == 0:
        return len(board)
    #at corners, we have 8
    else:
        #going forwards
        if (d_y, d_x) == (1, 1):
            return len(board) - max(y_start, x_start)
        #going backwards
        if (d_y, d_x) == (1, -1):
            if (y_start, x_start) == (0, len(board) - 1):
                return len(board)
            elif x_start != len(board) - 1:
                return 1 + x_start
            else:
                return len(board) - y_start
             
    
def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count , semi_open_seq_count = 0, 0

    cur_len = 0

    row_len = get_row_len(board, y_start, x_start, d_y, d_x)

    i = 0
    while i < row_len:
        #count length if the color matches
        if board[y_start + i*d_y][x_start + i*d_x] == col:
            cur_len += 1
        #if color doesn't match, analyze current sequence
        else:
            if cur_len == length:
                seq_type = is_bounded(board, y_start + (i - 1) * d_y, x_start + (i - 1) * d_x, length, d_y, d_x)
                if seq_type == "OPEN":
                    open_seq_count += 1
                    
                elif seq_type == "SEMIOPEN":
                    semi_open_seq_count += 1
                    
            cur_len = 0
        i += 1

    #If function exits for-loop, need to check again in case sequence is touching the border
    if cur_len == length:
        seq_type = is_bounded(board, y_start + (row_len - 1) * d_y, x_start + (row_len - 1) * d_x, length, d_y, d_x)
        if seq_type == "OPEN":
            open_seq_count += 1
            cur_len = 0
        elif seq_type == "SEMIOPEN":
            semi_open_seq_count += 1
            cur_len = 0
    else:
        cur_len = 0
    #Return final count
    return (open_seq_count, semi_open_seq_count)
    
def detect_rows(board, col, length):
    
    open_seq_count, semi_open_seq_count = 0, 0

    for i in range (len(board)):
        #Analyze every horizontal row
        hori = detect_row(board, col, i, 0, length, 0, 1)
        open_seq_count += hori[0]
        semi_open_seq_count += hori[1]

        #Analyze every vertical column
        verti = detect_row(board, col, 0, i, length, 1, 0)
        open_seq_count += verti[0]
        semi_open_seq_count += verti[1]

        #Analyze all left to right diagonals
        diag_1a = detect_row(board, col, i, 0, length, 1, 1)
        open_seq_count += diag_1a[0]
        semi_open_seq_count += diag_1a[1]

        diag_1b = detect_row(board, col, 0, i, length, 1, 1)
        open_seq_count += diag_1b[0]
        semi_open_seq_count += diag_1b[1]

    double_count1 = detect_row(board, col, 0, 0, length, 1, 1) #this diagonal is counted twice and must be subtracted from the sum
    open_seq_count -= double_count1[0]
    semi_open_seq_count -= double_count1[1]
    
    for i in range (len(board) - 1, -1, -1):
        #Analyze all right to left diagonals
        diag_2a = detect_row(board, col, 0, i, length, 1, -1)
        open_seq_count += diag_2a[0]
        semi_open_seq_count += diag_2a[1]

        diag_2b = detect_row(board, col, i, len(board) - 1, length, 1, -1)
        open_seq_count += diag_2b[0]
        semi_open_seq_count += diag_2b[1]

    double_count2 = detect_row(board, col, 0, len(board) - 1, length, 1, -1) #this diagonal is counted twice and must be subtracted from the sum
    open_seq_count -= double_count2[0]
    semi_open_seq_count -= double_count2[1]

    return (open_seq_count, semi_open_seq_count)

def detect_row3(board, col, y_start, x_start, length, d_y, d_x):
    open_seq_count , semi_open_seq_count, closed_seq_count = 0, 0, 0

    cur_len = 0

    row_len = get_row_len(board, y_start, x_start, d_y, d_x)

    i = 0
    while i < row_len:
        #count length if the color matches
        if board[y_start + i*d_y][x_start + i*d_x] == col:
            cur_len += 1
        #if color doesn't match, analyze current sequence
        else:
            if cur_len == length:
                seq_type = is_bounded(board, y_start + (i - 1) * d_y, x_start + (i - 1) * d_x, length, d_y, d_x)
                if seq_type == "OPEN":
                    open_seq_count += 1
                    
                elif seq_type == "SEMIOPEN":
                    semi_open_seq_count += 1
                
                elif seq_type == "CLOSED":
                    closed_seq_count += 1
                    
            cur_len = 0
        i += 1

    #If function exits for-loop, need to check again in case sequence is touching the border
    if cur_len == length:
        seq_type = is_bounded(board, y_start + (row_len - 1) * d_y, x_start + (row_len - 1) * d_x, length, d_y, d_x)
        if seq_type == "OPEN":
            open_seq_count += 1
            cur_len = 0
        elif seq_type == "SEMIOPEN":
            semi_open_seq_count += 1
            cur_len = 0
        elif seq_type == "CLOSED":
            closed_seq_count += 1
            cur_len = 0
    else:
        cur_len = 0
    #Return final count
    return (open_seq_count, semi_open_seq_count, closed_seq_count)
    
def detect_rows3(board, col, length):
    
    open_seq_count, semi_open_seq_count, closed_seq_count = 0, 0, 0

    for i in range (len(board)):
        #Analyze every horizontal row
        hori = detect_row3(board, col, i, 0, length, 0, 1)
        open_seq_count += hori[0]
        semi_open_seq_count += hori[1]
        closed_seq_count += hori[2]

        #Analyze every vertical column
        verti = detect_row3(board, col, 0, i, length, 1, 0)
        open_seq_count += verti[0]
        semi_open_seq_count += verti[1]
        closed_seq_count += verti[2]

        #Analyze all left to right diagonals
        diag_1a = detect_row3(board, col, i, 0, length, 1, 1)
        open_seq_count += diag_1a[0]
        semi_open_seq_count += diag_1a[1]
        closed_seq_count += diag_1a[2]


        diag_1b = detect_row3(board, col, 0, i, length, 1, 1)
        open_seq_count += diag_1b[0]
        semi_open_seq_count += diag_1b[1]
        closed_seq_count += diag_1a[2]

    double_count1 = detect_row3(board, col, 0, 0, length, 1, 1) #this diagonal is counted twice and must be subtracted from the sum
    open_seq_count -= double_count1[0]
    semi_open_seq_count -= double_count1[1]
    closed_seq_count -= double_count1[2]
    
    for i in range (len(board) - 1, -1, -1):
        #Analyze all right to left diagonals
        diag_2a = detect_row3(board, col, 0, i, length, 1, -1)
        open_seq_count += diag_2a[0]
        semi_open_seq_count += diag_2a[1]
        closed_seq_count += diag_2a[2]

        diag_2b = detect_row3(board, col, i, len(board) - 1, length, 1, -1)
        open_seq_count += diag_2b[0]
        semi_open_seq_count += diag_2b[1]
        closed_seq_count += diag_2b[2]

    double_count2 = detect_row3(board, col, 0, len(board) - 1, length, 1, -1) #this diagonal is counted twice and must be subtracted from the sum
    open_seq_count -= double_count2[0]
    semi_open_seq_count -= double_count2[1]
    closed_seq_count -= double_count2[2]

    return (open_seq_count, semi_open_seq_count, closed_seq_count)
    
def search_max(board):
    max_score = score(board)
    max_coords = [-1,-1]
    for i in range (len(board)):
        for j in range (len(board[0])):
            if board[i][j] == " ":
                put_seq_on_board(board, i, j, 0, 1, 1, 'b')
                cur_score = score(board)
                if cur_score > max_score:
                    max_score = cur_score
                    max_coords = [i, j]
                put_seq_on_board(board, i, j, 0, 1, 1, " ")

    return (max_coords[0], max_coords[1])

def score(board):
    MAX_SCORE = 100000
    
    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}
    
    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)
        
    
    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE
    
    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE
        
    return (-10000 * (open_w[4] + semi_open_w[4])+ 
            500  * open_b[4]                     + 
            50   * semi_open_b[4]                + 
            -100  * open_w[3]                    + 
            -30   * semi_open_w[3]               + 
            50   * open_b[3]                     + 
            10   * semi_open_b[3]                +  
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])

#HELPER FUNCTION
#Return True if board is full, False if not
def is_full_board(board):
    for i in range (len(board)):
        for j in range(len(board[0])):
            if board[i][j] == " ":
                return False
    return True
    
def is_win(board):
    for i in range (5, len(board)):
        num_black_seq = detect_rows3(board, "b", i)
        num_white_seq = detect_rows3(board, "w", i)

        if num_black_seq[0] >= 1 or num_black_seq[1] or num_black_seq[2] >= 1:
            return "Black won"
        
        elif num_white_seq[0] >= 1 or num_white_seq[1] or num_white_seq[2] >= 1:
            return "White won"

    if is_full_board(board):
        return "Draw"
    else:
        return "Continue playing"

def print_board(board):
    
    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"
    
    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1]) 
    
        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"
    
    print(s)
    

def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board
                


def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))
        
    
    

        
    
def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])
    
    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)
            
        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
            
            
        
        
        
        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)
        
        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res
        
            
            
def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col        
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    
    y_end = 3
    x_end = 5

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    
    y = 3; x = 5; d_x = -1; d_y = 1; length = 2
    
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)
    
    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #     
    
    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);
    
    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #        
    #        
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


  
            
if __name__ == '__main__':
    #Running built in test functions
    print ("RUNNING PROGRAM TESTS")
    print ("----------------------")
    print ("Easy Testset: ")
    easy_testset_for_main_functions()

    print ("Some Tests: ")
    some_tests()
    
