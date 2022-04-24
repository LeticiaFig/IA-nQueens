from nQueens import NQueens
import time
numberOfQueens = 9
numberOfIterations = 10
sum = 0

for x in range(numberOfIterations):
  t0= time.time()

  nqueens = NQueens(numberOfQueens, '123')
  nqueens.run()

  t1 = time.time() - t0

  sum += t1

print("Time elapsed: ", t1/15)