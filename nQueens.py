from random import random, sample, shuffle

from numpy import number 


class NQueens():
      
  def __init__(self, numberOfQueens, method, maxIterations) -> None:
      self.method = method
      self.numberOfQueens = numberOfQueens
      self.initialPositions = self.randomPositions()
      self.currentPositions = self.initialPositions 
      self.history = [self.initialPositions]    
      self.sumViolations = 0
      self.countIterations = 0      
      self.currentViolations = 0
      self.maxIterations = maxIterations
      self.solved = False

  def randomPositions(self):
    possiblePositions = list(range(1, self.numberOfQueens+1))
    
    while((possiblePositions[0] in [1, self.numberOfQueens]) 
      or possiblePositions[self.numberOfQueens-1] in [1, self.numberOfQueens]):
      shuffle(possiblePositions)
    
    return possiblePositions


  def run(self):
    print("\nProblema das ", self.numberOfQueens, " rainhas!\n")
    print("Tabuleiro inicial:")
    
    self.printBoard(self.initialPositions)
    self.hillClimb()
    self.printBoard(self.currentPositions)

    return { 'violations': self.sumViolations, 'solved': self.solved }
    #hillClimb()

  def hillClimb(self):
    self.currentViolations = self.counterOfAllViolations(self.initialPositions)
    
    while self.currentViolations > 0 and self.countIterations < self.maxIterations:
      self.sumViolations += self.currentViolations
      self.countIterations += 1

      print('Number of conflicts: ', self.currentViolations)
      
      # if(random()*10<2):
      #   neighboars = [sample(self.initialPositions, self.numberOfQueens)]        
      # else:
      #   neighboars = self.getAllNeighboards(self.currentPositions)

      # minViolations = violations
      # bestNeighboard = self.currentPositions

      # for neighboard in neighboars:
      #   currentViolations = self.counterOfAllViolations(neighboard)
        
      #   if(currentViolations < minViolations):
      #     minViolations = currentViolations
      #     bestNeighboard = neighboard
      #     break

      bestNeighboard = self.getBestNeighboard(self.currentPositions)
          

      self.currentPositions = bestNeighboard  
      self.history.append(self.currentPositions.copy())
      #violations = minViolations  

    print('Number of iterations: ', self.countIterations)
    if(self.currentViolations == 0): self.solved = True

  def getAllNeighboards(self, board):
    neighboards = []

    for i, line in enumerate(board):
      for j, line in enumerate(board[i+1: len(board)]):
        neighboard = board.copy()
        neighboard[i], neighboard[i+j+1] = neighboard[i+j+1], neighboard[i] 
        
        if(neighboard not in self.history):
          neighboards.append(neighboard)

    return neighboards 

  def getBestNeighboard(self, board):
    bestNeighboard = []

    for i, line in enumerate(board):
      for j, line in enumerate(board[i+1: len(board)]):
        neighboard = board.copy()
        neighboard[i], neighboard[i+j+1] = neighboard[i+j+1], neighboard[i] 

        currentViolations = self.counterOfAllViolations(neighboard)
        
        if(currentViolations < self.currentViolations and neighboard not in self.history):
          self.currentViolations = currentViolations
          bestNeighboard = neighboard
          break
  
    if(len(bestNeighboard) == 0 or random()*100<20):
      bestNeighboard = board.copy()
      shuffle(bestNeighboard)

    return bestNeighboard 


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
