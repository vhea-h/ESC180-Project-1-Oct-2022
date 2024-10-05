# hello thank you for using my tests
# make sure you put in same directory as gomoku file
# stuff in here could be wrong bc i am human too
# last updated: November 12, 2022, v3
# samson!

import gomoku as g

def check_answer(case, answer, result, board):

    # READ THIS:
    # if you want each test to output expected and result anyways
    # set the parameter below to True

    display_anyways = False
    # this will print the board, expected answer, and result each time
    # if this is False, the above will only print when you fail a test

    if answer != result:
        print(f"test case {case} FAILED :(")
        g.print_board(board)
        print(f"expected: {answer}, got: {result}")
    else:
        if display_anyways == True:
            g.print_board(board)
            print(f"expected: {answer}, got: {result}")
        print(f"test case {case} PASSED :)")

if __name__ == '__main__':

    # EDGE CASES FOR WINS
    # if you want to figure out what went wrong just put this
    # under the section of code: (failed tests will automatically print)
    # g.print_board(board)

    print("\n\nis_win tests:")
    # test 1: closed black (0, 1)
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 0, 0, 0, 1, 5, 'b')
    board[0][5] = 'w'
    check_answer(1, 'Black won', g.is_win(board), board)

    # test 2: closed black (1, 0)
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 0, 0, 1, 0, 5, 'b')
    board[5][0] = 'w'
    check_answer(2, 'Black won', g.is_win(board), board)

    # test 3: closed black (1, 1)
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 0, 0, 1, 1, 5, 'b')
    board[5][5] = 'w'
    check_answer(3, 'Black won', g.is_win(board), board)

    # test 4: open (1, -1)
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 1, 6, 1, -1, 5, "w")
    check_answer(4, 'White won', g.is_win(board), board)

    # test 5: semiopen (1, -1)
    board[0][7] = 'b'
    check_answer(5, 'White won', g.is_win(board), board)

    # test 6: closed(1, -1)
    board[6][1] = 'b'
    check_answer(6, 'White won', g.is_win(board), board)

    # test 7: Draw
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 0, 0, 0, 1, 8, 'b')
    g.put_seq_on_board(board, 1, 0, 0, 1, 8, 'b')
    g.put_seq_on_board(board, 2, 0, 0, 1, 8, 'b')
    g.put_seq_on_board(board, 3, 0, 0, 1, 8, 'b')
    g.put_seq_on_board(board, 4, 0, 0, 1, 8, 'b')
    g.put_seq_on_board(board, 5, 0, 0, 1, 8, 'b')
    g.put_seq_on_board(board, 6, 0, 0, 1, 8, 'b')
    g.put_seq_on_board(board, 7, 0, 0, 1, 8, 'b')
    check_answer(7, "Black won", g.is_win(board), board)

    # AI tests
    print("\n\nai tests")

    # test 1: blocks white from winning
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 0, 0, 1, 0, 4, 'w')
    check_answer(1, (4, 0), g.search_max(board), board)

    # test 2: wins over blocking
    g.put_seq_on_board(board, 0, 1, 1, 0, 4, 'b')
    check_answer(2, (4, 1), g.search_max(board), board)

    # test 3: chooses the right one to block
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 0, 7, 1, -1, 4, 'w')
    g.put_seq_on_board(board, 1, 0, 1, 0, 3, 'w')
    check_answer(3, (4, 3), g.search_max(board), board)

    # test 4: more block testing
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 0, 1, 0, 1, 3, 'b')
    g.put_seq_on_board(board, 1, 3, 1, 0, 4, 'w')
    check_answer(4, (5, 3), g.search_max(board), board)

    # test 5: creating open 4's for the win
    board[5][3] = 'b'
    check_answer(5, (0, 4), g.search_max(board), board)

    # test 6: find best move on a messy board
    board = g.make_empty_board(8)
    board[0][2] = 'w'
    board[2][2] = 'w'
    board[0][5] = 'w'
    g.put_seq_on_board(board, 1, 3, 1, 1, 3, 'b')
    board[1][4] = 'w'
    g.put_seq_on_board(board, 1, 5, 1, 0, 4, 'b')
    board[2][2] = 'w'
    board[2][7] = 'w'
    g.put_seq_on_board(board, 2, 3, 0, 1, 4, 'b')
    g.put_seq_on_board(board, 3, 3, 1, 0, 2, 'w')
    g.put_seq_on_board(board, 3, 4, 0, 1, 2, 'b')
    board[3][4] = 'b'
    board[4][4] = 'b'
    board[5][4] = 'w'
    board[1][7] = 'w'
    test = g.search_max(board)
    board[test[0]][test[1]] = 'b'
    check_answer(6, "Black won", g.is_win(board), board)

    # test 7: does your search max return invalid moves?
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 2, 4, 1, 0, 3, 'w')
    g.put_seq_on_board(board, 2, 0, 0, 1, 4, 'b')
    check_answer(7, (1, 4), g.search_max(board), board)


    # some basic tests on counting sequences
    print("\n\nbasic detect_rows tests")

    # test 1: 
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 1, 1, 1, 0, 3, 'b')
    g.put_seq_on_board(board, 1, 2, 1, 0, 3, 'b')
    g.put_seq_on_board(board, 1, 3, 1, 0, 3, 'b')
    check_answer(1, (8, 0), g.detect_rows(board, 'b', 3), board)

    # test 2:
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 0, 0, 1, 0, 3, 'b')
    g.put_seq_on_board(board, 0, 1, 1, 0, 3, 'b')
    g.put_seq_on_board(board, 0, 2, 1, 0, 3, 'b')
    g.put_seq_on_board(board, 5, 5, 1, 0, 3, 'b')
    g.put_seq_on_board(board, 5, 6, 1, 0, 3, 'b')
    g.put_seq_on_board(board, 5, 7, 1, 0, 3, 'b')
    check_answer(2, (0, 14), g.detect_rows(board, 'b', 3), board)

    # test 3:
    # notes that this test assumes BBBB_ does NOT
    # count as a semi open sequences of length 3
    g.put_seq_on_board(board, 0, 3, 1, 0, 3, 'b')
    g.put_seq_on_board(board, 3, 0, 0, 1, 3, 'b')
    g.put_seq_on_board(board, 4, 5, 0, 1, 3, 'b')
    g.put_seq_on_board(board, 5, 4, 1, 0, 3, 'b')
    check_answer(3, (2, 10), g.detect_rows(board, 'b', 3), board)

    # test 4, 5, 6, 7, 8:
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 1, 1, 1, 1, 6, 'b')
    check_answer(4, (0, 0), g.detect_row(board, 'b', 1, 1, 2, 1, 1), board)
    check_answer(5, (0, 0), g.detect_row(board, 'b', 2, 2, 3, 1, 1), board)
    check_answer(6, (0, 0), g.detect_row(board, 'b', 0, 0, 5, 1, 1), board)
    check_answer(7, (0, 0), g.detect_row(board, 'b', 0, 0, 4, 1, 1), board)
    # according to post 188 on piazza you will not be tested on this... (test 8)
    check_answer(8, "Continue playing", g.is_win(board), board)


    # according to post 141 on piazza we are not supposed to make improvements 
    # to the ai so in theory you should fail the tests below...

    # some more advanced tests on the AI 
    print("\n\nadvanced ai tests")
    # advanced test 1: open white 4, but black can win
    # this one requires you to make a better score(board) function
    # i dont think you will lose marks for getting this wrong
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 2, 1, 1, 1, 4, 'b')
    g.put_seq_on_board(board, 6, 2, 0, 1, 4, 'w')
    check_answer(1, (1, 0), g.search_max(board), board)
    print("THIS ONE IS SUPPOSED TO FAIL")
    print("IF YOU PASS YOU MUST REVERT YOUR AI BACK TO NORMAL")

    # advanced test 2: does this prevent white from winning when 
    # position is ww_ww or w_www
    # according to guerzhoy solving this requires knowledge from
    # beyond ESC180 so this wont be marked
    board = g.make_empty_board(8)
    board[5][5] = 'w'
    g.put_seq_on_board(board, 1, 1, 1, 1, 3, 'w')
    g.put_seq_on_board(board, 7, 1, 0, 1, 3, 'b')
    check_answer(2, (4, 4), g.search_max(board), board)
    print("THIS ONE IS SUPPOSED TO FAIL")
    print("IF YOU PASS YOU MUST REVERT YOUR AI BACK TO NORMAL")

    # advanced test 3: is it a win if there is a sequence of 6 on the board?
    # YOU SHOULD STILL PASS THIS ONE THOUGH
    board = g.make_empty_board(8)
    g.put_seq_on_board(board, 1, 1, 1, 1, 6, 'w')
    check_answer(3, "Continue playing", g.is_win(board), board)