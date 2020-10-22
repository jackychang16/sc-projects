"""
File: bouncing_ball
Name:JackyChang
-------------------------
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
sphere = GOval(SIZE, SIZE)
num = 0

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    global sphere
    sphere.filled = True
    sphere.fill_color = "black"
    window.add(sphere, START_X, START_Y)
    onmouseclicked(bouncing)


def bouncing(mouse):
    global sphere
    global num
    maybe_sphere = window.get_object_at(START_X+SIZE/2, START_Y+SIZE/2)
    if maybe_sphere is not None and num < 3:
        vy = 0
        while True:
            sphere.move(VX, vy)
            pause(DELAY)
            vy = vy + GRAVITY
            if sphere.y + sphere.height >= window.height:
                vy = -vy*0.9
            if sphere.x + sphere.width >= window.width:
                break
        window.add(sphere, START_X, START_Y)
        num += 1




if __name__ == "__main__":
    main()
