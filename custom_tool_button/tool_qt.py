from .common import *
import matplotlib.backends.backend_qt
from matplotlib.backends.qt_compat import QtGui, _enum, _devicePixelRatioF, _setDevicePixelRatio


_OldToolbarClass = matplotlib.backends.backend_qt.NavigationToolbar2QT


class _NavigationToolbar2Qt(_OldToolbarClass):
    def __init__(self, canvas, parent, coordinates=True):
        super().__init__(canvas, parent, coordinates=coordinates)
        for text, tooltip_text, image_file, callback in TOOLITEMS:
            a = self.addAction(self._fb_icon(image_file), text, callback(self))
            self._actions[callback] = a
            a.setCheckable(False)
            if tooltip_text is not None:
                a.setToolTip(tooltip_text)

    def _fb_icon(self, name):
        """
        Construct a `.QIcon` from an image file *name*, including the extension
        and relative to Matplotlib's "images" data directory.
        """
        pm = QtGui.QPixmap(name)
        _setDevicePixelRatio(pm, _devicePixelRatioF(self))
        if self.palette().color(self.backgroundRole()).value() < 128:
            icon_color = self.palette().color(self.foregroundRole())
            mask = pm.createMaskFromColor(QtGui.QColor('black'), _enum("QtCore.Qt.MaskMode").MaskOutColor)
            pm.fill(icon_color)
            pm.setMask(mask)
        return QtGui.QIcon(pm)


matplotlib.backends.backend_qt.NavigationToolbar2QT = _NavigationToolbar2Qt
