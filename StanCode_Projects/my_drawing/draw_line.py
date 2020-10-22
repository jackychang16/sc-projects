"""
File: draw_line.py
Name: JackyChang
-------------------------
This program helps you connect two spots with one line.
When you click the first time, the window will show the circle
in the cursor. And then when you click the second time, the window
will not only remove the last circle but show the line connected with that one.
In this programs, pairs as a group and so on except clicking in odd times,
the last circle will not be removed.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(title="draw_line")
SIZE = 20
old_x = 0
Old_y = 0
figure = 1
circle = GOval(SIZE, SIZE)


def main():
    onmouseclicked(draw)


def draw(mouse):
    global figure
    global old_x
    global old_y
    circle.x = mouse.x
    circle.y = mouse.y
    if figure % 2 == 1:
        old_x = circle.x
        old_y = circle.y
        circle.filled = True
        circle.fill_color = "white"
        circle.color = "black"
        window.add(circle, circle.x-circle.width//2, circle.y-circle.height//2)
        figure += 1
    else:
        window.remove(circle)
        line = GLine(old_x, old_y, circle.x, circle.y)
        line.filled = True
        line.filled_color = "black"
        window.add(line)
        figure += 1


if __name__ == "__main__":
    main()
