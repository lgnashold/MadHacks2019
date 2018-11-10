BOARD_WIDTH = 3
BOARD_HEIGHT = 3
DEFAULT_SQUARE = {"color":"ff0055"}

import json

from boardgame.db import get_db


def create_board(join_code):
    print("called create board")
    board = []
    for row in range(BOARD_WIDTH):
            board.append([])
            for col in range(BOARD_HEIGHT):
                board[row].append(DEFAULT_SQUARE)
    set_board(board, join_code)
    return board

def set_board(board, join_code):
    """Given a board array, saves it to sql database"""
    json_board = json.dumps(board)
    print(json_board)
    db = get_db()
    db.execute(
            'UPDATE game SET game_data = (?) WHERE join_code = (?)', (json_board, join_code)
    );
    db.commit();
    return json_board

def get_board(join_code):
    return json.loads(get_json_board(join_code))


def get_json_board(join_code):
    db = get_db()
    json_board = db.execute(
            "SELECT game_data FROM game WHERE join_code = (?)", (join_code,)
    ).fetchone()["game_data"]
    return json_board