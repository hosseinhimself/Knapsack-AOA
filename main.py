import numpy as np
import matplotlib.pyplot as plt
from AOA import AOA
import knapsack

knapsack = knapsack.model(n = 70, W = 10000)

Max_iter = 400
dim = 1

#C3=2 
#C4=0.5   #cec and engineering problems
C3 = 1
C4 = 2

Xbest, Scorebest, Convergence_curve, Y = AOA(knapsack, Max_iter, dim, C3, C4)
print("Best Solution:",Xbest)
print("cost of best solution: ", Scorebest)

try:
    unique, counts = np.unique(Xbest, return_counts=True)
    print('The number of items in the knapsack:', counts[1])
except:
    print("problem")

print('Capacity of knapsack:',knapsack.W)

filter = []
for material in Xbest:
    if material == 1:
        filter.append(True)
    else:
        filter.append(False)

sum_of_weights = sum(knapsack.w[filter])
print("Sum of weights: ",sum_of_weights)

plt.semilogy(np.arange(Max_iter), Convergence_curve)

font1 = {'color':'purple','size':20}
font2 = {'color':'darkred','size':15}

plt.ylabel("Cost Function", fontdict = font2)
plt.xlabel("Iterations", fontdict = font2)

plt.title("Knapsack Problem Solution Using AOA", fontdict = font1)
plt.show()