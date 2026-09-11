from tennis import TennisGame

def add_points(game, p1Score, p2Score):
    for x in range(p1Score):
        game.p1ScoresPoint()
    for x in range(p2Score):
        game.p2ScoresPoint()

def test_new_game_is_love_all():
    game = TennisGame()

    assert game.score() == "Love-All"

def test_p1_scores_a_point():
    game = TennisGame()
    add_points(game, 1, 0)

    assert game.score() == "Fifteen-Love"

def test_p2_and_p1_scores_a_point():
    game = TennisGame()
    add_points(game, 1, 1)

    assert game.score() == "Fifteen-All"

def test_p1_scores_3_without_reply():
    game = TennisGame()
    add_points(game, 3, 0)

    assert game.score() == "Fourty-Love"

def test_p1_p2_score_deuce():
    game = TennisGame()

    add_points(game, 3, 3)

    assert game.score() == "Deuce"

def test_p1_wins_game():
    game = TennisGame()

    add_points(game, 4, 0)

    assert game.score() == "Player 1 wins"

def test_p2_wins_game():
    game = TennisGame()

    add_points(game, 0, 4)

    assert game.score() == "Player 2 wins"

def test_p1_gain_advantage():
    game = TennisGame()

    add_points(game, 5, 4)

    assert game.score() == 'Advantage Player 1'

def test_p2_gain_advantage():
    game = TennisGame()

    add_points(game, 4, 5)

    assert game.score() == 'Advantage Player 2'

def test_p1_gain_advantage_and_winner():
    game = TennisGame()

    add_points(game, 3, 3)

    add_points(game, 1, 0)
    assert game.score() == 'Advantage Player 1'

    add_points(game, 1, 0)
    assert game.score() == 'Player 1 wins'

def test_p1_gain_advantage_and_loses_it_for_deuce():
    game = TennisGame()

    add_points(game, 3, 3)

    add_points(game, 1, 0)
    assert game.score() == 'Advantage Player 1'

    add_points(game, 0, 1)
    assert game.score() == 'Deuce'

def test_p1_gain_advantage_after_deuce_to_win():
    game = TennisGame()

    add_points(game, 3, 3)

    add_points(game, 1, 0)
    assert game.score() == 'Advantage Player 1'

    add_points(game, 0, 1)
    assert game.score() == 'Deuce'

    add_points(game, 1, 0)
    assert game.score() == 'Advantage Player 1'

    add_points(game, 1, 0)
    assert game.score() == 'Player 1 wins'

def test_p2_gain_advantage_after_deuce_to_win():
    game = TennisGame()

    add_points(game, 3, 3)

    add_points(game, 0, 1)
    assert game.score() == 'Advantage Player 2'

    add_points(game, 1, 0)
    assert game.score() == 'Deuce'

    add_points(game, 0, 1)
    assert game.score() == 'Advantage Player 2'

    add_points(game, 0, 1)
    assert game.score() == 'Player 2 wins'

"""
Test cases I need to cover:

Each player could have love, fifteen, thirty, fourty - done
Players on equal score but less than or equal to thirty will be announced thirty all for example - done
Players on equal score but both have at least 40 points, will be announced DEUCE - done
Players on more than 40 and a clear 2 point difference, will be announced winner - done
Players on more than 40 but less than 2 point difference, will be announced ADV - done
Player with ADV winning the point, will be announced winner 
Player without ADV winning the point, will be announced DEUCE

"""