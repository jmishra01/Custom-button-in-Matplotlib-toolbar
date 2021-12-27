import matplotlib

backend = matplotlib.rcParams["backend"]
print("Matplotlib's backend - ", backend)
if backend == "TkAgg":
    from . import tool_tk as tool
elif backend == "QtAgg":
    from . import tool_qt as tool
else:
    raise ImportError("Not implement yet")
