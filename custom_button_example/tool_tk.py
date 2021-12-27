from .common import *
import matplotlib.backends.backend_tkagg
import matplotlib.backends


_OldToolbarClass = getattr(matplotlib.backends, '_backend_tk').NavigationToolbar2Tk
Tooltip = getattr(matplotlib.backends, '_backend_tk').ToolTip


class _NavigationToolbar2Tk(_OldToolbarClass):
    def __init__(self, canvas, window, *, pack_toolbar=True):
        super().__init__(canvas, window, pack_toolbar=pack_toolbar)

        for text, tooltip_text, image_file, callback in TOOLITEMS:
            self._buttons[text] = button = self._Button(text, image_file, toggle=False, command=callback(self))
            if tooltip_text is not None:
                Tooltip.createToolTip(button, tooltip_text)


getattr(matplotlib.backends, '_backend_tk').NavigationToolbar2Tk = _NavigationToolbar2Tk
