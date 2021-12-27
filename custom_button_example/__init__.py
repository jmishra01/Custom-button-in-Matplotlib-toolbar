import matplotlib


print("Matplotlib's backend - ", matplotlib.rcParams["backend"])
if matplotlib.rcParams["backend"] == "TkAgg":
    from . import tool_tk as mcl
elif matplotlib.rcParams["backend"] == "QtAgg":
    from . import tool_qt as mcl
else:
    raise ImportError("Not implement yet")

