from tennis import TennisGame


def test_new_game_is_love_all():
    game = TennisGame()

    assert game.score() == "Love-All"

def test_p1_scores_a_point():
    game = TennisGame()
    game.p1ScoresPoint()

    assert game.score() == "Fifteen-Love"