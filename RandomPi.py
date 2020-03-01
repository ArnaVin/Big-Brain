# Randomly Generate number from 0 to 1
# Calculate the number pi

import random
import matplotlib.pyplot as plt

X = []
Y = []
def estimate_pi(n):
    circle_point = 0
    square_point = 0
    for _ in range(n):
        x = random.uniform(0,1)
        X.append(x)
        y = random.uniform(0,1)
        Y.append(y)
        distance = x**2+y**2
        if distance <= 1:
            circle_point += 1
        square_point += 1
        
    return 4*circle_point/square_point
 

print('Enter the number of random numbers :')
pi_ish = estimate_pi(int(input()))
print(pi_ish)

plt.scatter(X,Y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Estimating\nPi')
plt.show()