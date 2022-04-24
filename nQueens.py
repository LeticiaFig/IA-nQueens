from random import random, sample 


class NQueens():
      
  def __init__(self, numberOfQueens, method) -> None:
      self.method = method
      self.numberOfQueens = numberOfQueens
      self.initialPositions = list(range(1, numberOfQueens+1)) 
      self.currentPositions = self.initialPositions 
      self.history = [self.initialPositions]          

  def run(self):
    print("\nProblema das ", self.numberOfQueens, " rainhas!\n")
    print("Tabuleiro inicial:")
    
    self.printBoard(self.initialPositions)
    self.hillClimb()
    self.printBoard(self.currentPositions)
    #hillClimb()

  def hillClimb(self):
    violations = self.counterOfAllViolations(self.initialPositions)
    
    while violations > 0:
      # print('Number of conflicts: ', violations)
      
      if(random()*10<2):
        neighboars = [sample(self.initialPositions, self.numberOfQueens)]        
      else:
        neighboars = self.getAllNeighboards(self.currentPositions)

      minViolations = violations
      bestNeighboard = self.currentPositions

      for neighboard in neighboars:
        currentViolations = self.counterOfAllViolations(neighboard)
        
        if(currentViolations < minViolations):
          minViolations = currentViolations
          bestNeighboard = neighboard
          break
          

      self.currentPositions = bestNeighboard  
      violations = minViolations  
      self.history.append(self.currentPositions.copy())

  def getAllNeighboards(self, board):
    neighboards = []

    for i, line in enumerate(board):
      for j, line in enumerate(board[i+1: len(board)]):
        neighboard = board.copy()
        neighboard[i], neighboard[i+j+1] = neighboard[i+j+1], neighboard[i] 
        
        if(neighboard not in self.history):
          neighboards.append(neighboard)

    return neighboards

  def counterOfAllViolations(self, board):
    return sum(self.counterViolationsByLine(board))

  def counterViolationsByLine(self, board):
    violations = [0]*self.numberOfQueens

    for i, line in enumerate(board):
      violations[i] += self.violationCounter(board, i)
      
    return violations


  def violationCounter(self, board, i):
    violations = 0
    
    for j, line in enumerate(board[i+1: len(board)]):
      if(board[i] == board[i+j+1]):
        violations += 1  
      if(abs(board[i]-board[i+j+1]) == j+1):
        violations += 1        
    return violations


  def printBoard(self, board):
    print('____________________')
    for position in board:
      line=['-']*self.numberOfQueens
      line[position-1]='Q'
      print(line)

    print('____________________')
