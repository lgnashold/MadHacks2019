from boardgame.db import get_db

import json

def add_player(join_code, nickname, money=300, team=None):
    """Adds a player to the game
    If games full, returns None, otherwise return player"""
    db = get_db()
    players = get_players(join_code)
    player_obj = {}

    player_obj["money"] = money
    player_obj["nickname"] = nickname

    count = 0
    for key, value in players.items():
        count+=1
        if value == None:
            player_obj["team"] = "team" + str(count)
            db.execute(
                    "UPDATE game SET %s = (?) WHERE join_code = (?)" % key, (json.dumps(player_obj), join_code)
                    )
            db.commit()
            session["player_num"] = count
            return player_obj
    return None

def remove_player(join_code, nickname):
    """Removes player from a game"""
    pass

def get_players(join_code):
    """returns a dictonary of all players in a game"""
    db = get_db()
    player_jsons = dict(db.execute(
            "SELECT player1, player2, player3, player4 FROM game WHERE join_code = (?)", (join_code,)).fetchone())
    players = {}
    for key, value in player_jsons.items():
        if value != None:
            players[key] = json.loads(value)
        else:
            players[key] = None
    return players

def get_player(join_code,nickname):
    players = get_players(join_code)
    for key, value in players:
        if(value['nickname'] == nickname):
            return value
    return none

def update_player_money(join_code,nickname,moneyChange):
    db = get_db()
    old_player = get_player(join_code,nickname)
    if old_playe == None:
        return None
    player_obj = {}

    player_obj["money"] = old_player["money"] + moneyChange
    player_obj["nickname"] = old_player["nickname"]
    player_obj["team"] = old_player["team"]

    db.execute(
            "UPDATE game SET %s = (?) WHERE join_code = (?)" % key, (json.dumps(player_obj), join_code)
            )
    db.commit()