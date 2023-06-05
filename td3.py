




# %% Exercice 3 

import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)

plt.plot(x,y, 'ro-')
plt.show()


# %% Exercice 4 

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi, 0.2)
y = np.sin(x)

plt.plot(x,y, 'ro-')
plt.show()