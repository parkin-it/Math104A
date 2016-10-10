#Solution to problem 1.3: 6                                                                                                                                                          

import numpy as np
import matplotlib.pyplot as plt


#Plot of Equation fo Problem 6a
x = np.linspace(0, 10, 200)
y = np.sin(1/x)

plt.figure()

plt.plot(x, y)

plt.grid(True)
plt.xlabel("n")
plt.title("6a")

plt.savefig("6a.png")

#Print the first 10 values of the limit
for i in range(1,10):
    print("Value n = "+ str(i) +": "+ str(np.sin(1/i)))


#Plot of Equation fo Problem 6b
x = np.linspace(0, 10, 200)
y = np.sin(1/x**2)

plt.figure()

plt.plot(x, y)

plt.grid(True)
plt.xlabel("n")
plt.title("6b")

plt.savefig("6b.png")

#Print the first 10 values of the limit
for i in range(1,10):
    print("Value n = "+ str(i) +": "+ str(np.sin(1/i**2)))

#Plot of Equation fo Problem 6c
x = np.linspace(0, 10, 200)
y = (np.sin(1/x))**2

plt.figure()

plt.plot(x, y)

plt.grid(True)
plt.xlabel("n")
plt.title("6c")

plt.savefig("6c.png")

#Print the first 10 values of the limit
for i in range(1,10):
    print("Value n = "+ str(i) +": "+ str((np.sin(1/i)**2)))

#Plot of Equation fo Problem 6d
x = np.linspace(0, 10, 200)
y = np.log(x+1) - np.log(x)

plt.figure()

plt.plot(x, y)

plt.grid(True)
plt.xlabel("n")
plt.title("6d")

plt.savefig("6d.png")

#Print the first 10 values of the limit
for i in range(1,10):
    print("Value n = "+ str(i) +": "+ str(np.log(i+1) - np.log(i)))