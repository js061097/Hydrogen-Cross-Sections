import numpy as np
from matplotlib import pyplot as plt

n = np.array([1,2,3])

#A = [0.18450, -0.032226, -0.034539, 1.4003, -2.8115, 2.2986]
A = [[0.18450, -0.032226, -0.034539, 1.4003, -2.8115, 2.2986],
    [0.14784, 0.0080871, -0.062270, 1.9414, -2.1980, 0.95894],
    [0.058463, -0.051272, 0.85310, -0.57014, 0.76684, 0.0]]

#Ionization Energy
In = 13.6/(n**2)

x_vals = np.array([np.linspace(In[i],200,270) for i in range(3)])
y_vals = np.zeros((3,270))

for i in range(3):
    prefactor = (10**(-17)/In[i]/x_vals[i])
    y_vals[i] =  (A[i][0]*np.log(x_vals[i]/In[i]))
    for j in range(1,6):
        y_vals[i] += A[i][j]*(1-(In[i]/x_vals[i]))**j
    y_vals[i] *= prefactor

for j in range(0,6):
    print(str(x_vals[0][j]) + " " + str(y_vals[0][j]))

for i in range(3):
    plt.loglog(x_vals[i],y_vals[i],label='H(n = ' + str(i+1) + ')')

plt.grid(True, which="both", ls="--", lw=0.7, alpha=0.7)
plt.ylabel('Cross-section '+'$(\mathrm{m}^{2})$')
plt.xlabel('Energy ' + '$(eV)$')
plt.title('Ionization Cross-section for electronically excited atomic H')
plt.legend()
plt.show()
