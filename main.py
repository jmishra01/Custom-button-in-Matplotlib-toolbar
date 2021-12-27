
"""
In matplotlib, default backend is QtAgg, to change it to TkAgg, uncomment below two lines
"""

import matplotlib
matplotlib.rcParams["backend"] = "tkagg"

from custom_button_example import *

import matplotlib.pyplot as plt
import numpy as np

mcl.SHIFT = 5

x = np.linspace(-10, 100, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.xlim([mcl.XAXIS_LIST[mcl.LEFT_POSI], mcl.XAXIS_LIST[mcl.RIGHT_POSI]])

plt.show()

