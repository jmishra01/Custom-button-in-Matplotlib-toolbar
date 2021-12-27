
import os
import numpy as np
"""
In matplotlib, default backend is QtAgg, to change it to TkAgg, uncomment below two lines
"""
# import matplotlib
# matplotlib.rcParams["backend"] = "tkagg"

from custom_tool_button import tool


icons = tool.Icons(os.path.dirname(__file__))


def tooltip_func(cls_instance):
    def wrapper(): 
        print('Custom tool button example.')
    return wrapper


tool.TOOLITEMS = [("Python Icon", "Tooltip Python icon", icons.icon_path("pyicon.png"), tooltip_func)]


import matplotlib.pyplot as plt

tool.SHIFT = 5

x = np.linspace(-10, 100, 1000)
y = np.sin(x)

plt.plot(x, y)
plt.xlim([tool.XAXIS_LIST[tool.LEFT_POSI], tool.XAXIS_LIST[tool.RIGHT_POSI]])

plt.show()

