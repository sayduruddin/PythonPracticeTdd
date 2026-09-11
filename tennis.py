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

  def calculateAdvantage(self):
     if (self.player1Score > 4 and self.player1Score > self.player2Score):
        return 'Advantage Player 1'
     elif (self.player2Score > 4 and self.player2Score > self.player1Score):
        return 'Advantage Player 2'

  def calculateWinner(self):
    if self.player1Score == self.player2Score:
        return 'Deuce'

    elif self.player1Score >= 4 and self.player1Score >= self.player2Score + 2:
        return 'Player 1 wins'

    elif self.player2Score >= 4 and self.player2Score >= self.player1Score + 2:
        return 'Player 2 wins'

    else:
       return self.calculateAdvantage()

    
  
  def score(self):
    # If score is equal but less than 40 on scoreboard, can use -All
    if (self.player1Score == self.player2Score and (self.player1Score < 3)):
      return f'{self.scoreMap.get(self.player1Score)}-All'
    # if score is equal but requires deuce
    elif (self.player1Score == self.player2Score):
       return 'Deuce'
    # if either player has more than or equal to 4 points, love, 15, 30, 40, winner = 4
    elif (self.player1Score >= 4 or self.player2Score >= 4):
      return self.calculateWinner()
    else:
      return f'{self.scoreMap[self.player1Score]}-{self.scoreMap[self.player2Score]}'

  def p1ScoresPoint(self):
    self.player1Score += 1

  def p2ScoresPoint(self):
    self.player2Score += 1