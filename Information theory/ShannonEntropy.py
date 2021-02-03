#%%
import numpy as np
import matplotlib.pyplot as plt

# Define the parameter p for the binary distribution
p = np.arange(0, 1, 1e-6)

# PDF of a binary distribution
# Input:
#   k = 0, 1
# Output:
#   binary distribution
def P_b(k):
  return p**k * (1-p)**(1-k)

# Shannon information
# Input:
#   P: PDF of a random variable
# Output:
#   Self-information in units of Shannon
def I(P):
  return -np.log(P)

# Shannon entropy
H = P_b(0) * I(P_b(0)) + P_b(1) * I(P_b(1))

# Expectation value
# Input:
#   func: function of a random variable whose expectation value is to be calculated
#   P: PDF of a random variable
# Output:
#   Self-information in units of Shannon
def E(func, P):
  if len(x) == len(P):
    count = 0
    for i in range(len(x)):
      count = count + x[i]*P[i]

plt.plot(p, H)
plt.title('Shannon entropy of a binary random variable')
plt.xlabel('p'); plt.ylabel('Shannon entropy in nats')
plt.xlim(0, 1); plt.ylim(0, 0.7)
plt.grid()
# %%
