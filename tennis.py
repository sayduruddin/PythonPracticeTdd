class TennisGame():
  scoreMap = {
    0: "Love",
    1: "Fifteen",
    2: "Thirty",
    3: "Fourty"
  }

  def __init__(self):  
      self.player1Score = 0
      self.player2Score = 0
  
  def score(self):
    if (self.player1Score == 0 & self.player2Score == 0):
      return 'Love-All'
    else:
      return f'{self.scoreMap[self.player1Score]}-{self.scoreMap[self.player2Score]}'

  def p1ScoresPoint(self):
    self.player1Score += 1

  def p2ScoresPoint(self):
    self.player2Score += 1