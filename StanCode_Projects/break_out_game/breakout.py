"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()

    while True:
        global NUM_LIVES
        if graphics.switch and NUM_LIVES > 0:
            graphics.rebound_the_wall()
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            graphics.rebound_the_paddle()
            graphics.remove_brick()
            graphics.win()
            if graphics.ball.y > graphics.window.height:
                NUM_LIVES -= 1
                graphics.restart()  # turn off switch and reset the initial speed
        pause(FRAME_RATE)

        if NUM_LIVES == 0:
            graphics.the_end()
            break


if __name__ == '__main__':
    main()
