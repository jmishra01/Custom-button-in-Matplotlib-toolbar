# Custom-toolbar-button

You can add custom icon on matplotlib toolbar, and there callback function.
 
```python
import os

# import custom_tool_button before matplotlib pyplot 
from custom_tool_button import tool

import matplotlib.pyplot as plt

# ----- Your code ---- #
```

![Forward Backward icon](https://raw.githubusercontent.com/jmishra01/Custom-button-in-Matplotlib-toolbar/main/example/forward_backward_icon.png?raw=true)


```python
import os

# import custom_tool_button before matplotlib pyplot 
from custom_tool_button import tool

icons = tool.Icons(os.path.dirname(__file__))


def tooltip_func(cls_instance):
    def wrapper(): 
        print('Custom tool button example.')
    return wrapper


tool.TOOLITEMS = [("Python Icon", "Tooltip Python icon", icons.icon_path("pyicon.png"), tooltip_func)]


import matplotlib.pyplot as plt

# ----- Your code ---- #
```

![Custom Python icon](https://raw.githubusercontent.com/jmishra01/Custom-button-in-Matplotlib-toolbar/main/example/custom_python_icon.png)
