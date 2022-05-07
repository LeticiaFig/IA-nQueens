from nQueens import NQueens
import time
numberOfQueens = 30
numberOfIterations = 10
maxInterations = 100
sum = 0
sumConflicts = 0
solvedBoards = 0

for x in range(numberOfIterations):
  t0= time.time()

  nqueens = NQueens(numberOfQueens, '123', maxInterations)
  response = nqueens.run()
  sumConflicts += response['violations']
  if(response['solved']): solvedBoards += 1

  t1 = time.time() - t0

  sum += t1

print("Time elapsed: ", t1/numberOfIterations)
print("Conflicts Average: ", sumConflicts/numberOfIterations)
print("Quantity Solved Boards: ", solvedBoards)