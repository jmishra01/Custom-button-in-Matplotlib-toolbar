import os

DIRECTORY = os.path.dirname(__file__)
IMAGE_DIRECTORY = os.path.join(DIRECTORY, 'images')


XAXIS_LIST = list(range(-10, 100))
LEFT_POSI = 0
RIGHT_POSI = 10
SHIFT = 10


class Icons:
    def __init__(self, dir_path):
        self._dir_path = dir_path

    def get_path(self) -> str:
        return self._dir_path

    def icon_path(self, im_path: str) -> str:
        return os.path.join(self._dir_path, im_path)


def update_canvas(cls_instance):
    cls_instance.canvas.draw_idle()


def fb_shift(cls_instance, x_lower_value, x_higher_value):
    cls_instance.canvas.figure.gca().set_xlim(x_lower_value, x_higher_value)
    update_canvas(cls_instance)


def backward_shift(cls_instance):
    def wrapper():
        global LEFT_POSI, RIGHT_POSI
        try:
            LEFT_POSI -= SHIFT
            RIGHT_POSI -= SHIFT
            fb_shift(cls_instance, XAXIS_LIST[LEFT_POSI], XAXIS_LIST[RIGHT_POSI])
        except IndexError:
            LEFT_POSI += SHIFT
            RIGHT_POSI += SHIFT
    return wrapper


def forward_shift(cls_instance):
    def wrapper():
        global LEFT_POSI, RIGHT_POSI
        try:
            LEFT_POSI += SHIFT
            RIGHT_POSI += SHIFT
            fb_shift(cls_instance, XAXIS_LIST[LEFT_POSI], XAXIS_LIST[RIGHT_POSI])
        except IndexError:
            LEFT_POSI -= SHIFT
            RIGHT_POSI -= SHIFT
    return wrapper


icons = Icons(IMAGE_DIRECTORY)

TOOLITEMS = [('Backward Shift', 'Shift chart backward', icons.icon_path('bshift.png'), backward_shift),
             ('Forward Shift', 'Shift chart forward', icons.icon_path('fshift.png'), forward_shift)]

