import os

DIRECTORY = os.path.dirname(__file__)
IMAGE_DIRECTORY = os.path.join(DIRECTORY, 'images')


XAXIS_LIST = list(range(-10, 100))
LEFT_POSI = 0
RIGHT_POSI = 10
SHIFT = 10

def fb_shift(cls_instance, x_lower_value, x_higher_value):
    cls_instance.canvas.figure.gca().set_xlim(x_lower_value, x_higher_value)
    cls_instance.canvas.draw_idle()


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


TOOLITEMS = [('Backward Shift', 'Shift chart backward', os.path.join(IMAGE_DIRECTORY, 'bshift.png'), backward_shift),
           ('Forward Shift', 'Shift chart forward', os.path.join(IMAGE_DIRECTORY, 'fshift.png'), forward_shift)
           ]

