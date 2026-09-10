from tennis import TennisGame


def test_new_game_is_love_all():
    game = TennisGame()

    assert game.score() == "Love-All"

def test_p1_scores_a_point():
    game = TennisGame()
    game.p1ScoresPoint()

    assert game.score() == "Fifteen-Love"

def test_p2_and_p1_scores_a_point():
    game = TennisGame()
    game.p1ScoresPoint()
    game.p2ScoresPoint()

    assert game.score() == "Fifteen-All"

def test_p1_scores_3_without_reply():
    game = TennisGame()
    game.p1ScoresPoint()
    game.p1ScoresPoint()
    game.p1ScoresPoint()

    assert game.score() == "Fourty-Love"

def test_p1_p2_score_deuce():
    game = TennisGame()

    game.p1ScoresPoint()
    game.p1ScoresPoint()
    game.p1ScoresPoint()

    game.p2ScoresPoint()
    game.p2ScoresPoint()
    game.p2ScoresPoint()

    assert game.score() == "Deuce"

def test_p1_wins_game():
    game = TennisGame()

    game.p1ScoresPoint()
    game.p1ScoresPoint()
    game.p1ScoresPoint()
    game.p1ScoresPoint()

    assert game.score() == "Player 1 wins"

def test_p2_wins_game():
    game = TennisGame()

    game.p2ScoresPoint()
    game.p2ScoresPoint()
    game.p2ScoresPoint()
    game.p2ScoresPoint()

    assert game.score() == "Player 2 wins"