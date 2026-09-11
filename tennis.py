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

  def p1ScoresPoint(self):
     self.player1Score += 1
  
  def p2ScoresPoint(self):
     self.player2Score += 1

  def calculateAdvantage(self):
     if (self.player1Score >= 4 and self.player1Score > self.player2Score):
        return 'Advantage Player 1'
     elif (self.player2Score >= 4 and self.player2Score > self.player1Score):
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

  def calculateTie(self):
     if (self.player1Score < 3):
        return f'{self.scoreMap.get(self.player1Score)}-All'

     return 'Deuce'
        
  
  def score(self):
   if self.player1Score == self.player2Score:
      return self.calculateTie()
   
   elif (self.player1Score >= 4 or self.player2Score >= 4):
      return self.calculateWinner()
   
   return f'{self.scoreMap[self.player1Score]}-{self.scoreMap[self.player2Score]}'
