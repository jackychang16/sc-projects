"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 10  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title="Breakout"):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title="title")

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=(self.window.height - self.paddle.height - paddle_offset))

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)

        self.switch = False
        self.removed_num = 0
        self.total = brick_rows*brick_cols
        # Default initial velocity for the ball.
        # Initialize our mouse listeners.
        onmouseclicked(self.switch_on)
        onmousemoved(self.paddle_reset_position)
        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                # filled different colors in sequence
                if j % 10 == 0 or j % 10 == 1:
                    self.brick.fill_color = "red"
                    self.brick.color = "red"
                elif j % 10 == 2 or j % 10 == 3:
                    self.brick.fill_color = "orange"
                    self.brick.color = "orange"
                elif j % 10 == 4 or j % 10 == 5:
                    self.brick.fill_color = "yellow"
                    self.brick.color = "yellow"
                elif j % 10 == 6 or j % 10 == 7:
                    self.brick.fill_color = "green"
                    self.brick.color = "green"
                elif j % 10 == 8 or j % 10 == 9:
                    self.brick.fill_color = "blue"
                    self.brick.color = "blue"
                self.window.add(self.brick, i * (BRICK_WIDTH + BRICK_SPACING), brick_offset+j * (BRICK_HEIGHT +BRICK_SPACING))

        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        # given a random figure in MAX_X_SPEED
        self.initial_vx = random.randint(1, MAX_X_SPEED)
        self.__dx = self.initial_vx
        # randomly create east or west direction in the start
        if random.random() > 0.5:
            self.__dx = -self.__dx

    # confine the movement range of the paddle
    def paddle_reset_position(self, mouse):
        if mouse.x >= (self.window.width - self.paddle.width):
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x <= self.paddle.width:
            self.paddle.x = 0
        elif mouse.x <= (self.window.width - self.paddle.width):
            self.paddle.x = mouse.x - self.paddle.width // 2

    # create a switch to control whether the program runs
    def switch_on(self, mouse):
        self.switch = True

    # because of __ can not changed
    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy

    # reset the ball and give it random speed in the same way as before ; turn off the switch.
    def restart(self):
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)
        initial_vx = random.randint(1, MAX_X_SPEED)
        self.__dx = initial_vx
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.switch = False

   # ball hit the wall will rebound in a regular way
    def rebound_the_wall(self):
        if 0 >= self.ball.x or self.ball.x >= (self.window.width - self.ball.width):
            self.__dx = -self.__dx
        if self.ball.y <= 0:
            self.__dx = -self.__dx
            self.__dy = -self.__dy

    # ball hit the paddle will rebound in a regular way
    def rebound_the_paddle(self):
        maybe_paddle_1 = self.window.get_object_at(self.ball.x, self.ball.y+self.ball.height)
        maybe_paddle_2 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        if maybe_paddle_1 == self.paddle and self.ball.y > self.window.height//2:
            self.__dy = -INITIAL_Y_SPEED
        elif maybe_paddle_2 == self.paddle and self.ball.y > self.window.height//2:
            self.__dy = -INITIAL_Y_SPEED

    def remove_brick(self):
        maybe_brick_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_brick_2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        maybe_brick_3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        maybe_brick_4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y+self.ball.height)
        if maybe_brick_1 is not None and self.ball.y < self.window.height//2:
            self.window.remove(maybe_brick_1)
            self.__dy = -self.__dy
            self.removed_num += 1

        # elif maybe_brick_2 == self.brick:
        elif maybe_brick_2 is not None and self.ball.y < self.window.height//2:
            self.window.remove(maybe_brick_2)
            self.__dx = -self.__dx
            self.__dy = -self.__dy

        elif maybe_brick_3 is not None and self.ball.y < self.window.height//2:
            self.window.remove(maybe_brick_3)
            self.__dx = -self.__dx
            self.__dy = -self.__dy

        elif maybe_brick_4 is not None and self.ball.y < self.window.height // 2:
            self.window.remove(maybe_brick_4)
            self.__dx = -self.__dx
            self.__dy = -self.__dy

    def win(self):
        if self.removed_num == self.total:
            blank = GRect(self.window.width,self.window.height)
            blank.filled = True
            blank.fill_color = "white"
            blank.color = "white"
            win_label = GLabel("you win!")
            win_label.color = "red"
            win_label.font = "-80"
            self.window.add(blank)
            self.window.add(win_label, x=(self.window.width-win_label.width/2), y=self.window.height/2)

    def the_end(self):
        label = GLabel("you lose!")
        label.color = "red"
        label.font = "-80"
        white_rect = GRect(self.ball.width, self.ball.height)
        white_rect.filled = True
        white_rect.fill_color = "white"
        white_rect.color = "white"
        self.window.add(label, x=(self.window.width-label.width)/2,y=self.window.height/2)
        self.window.add(white_rect, x=self.ball.x, y=self.ball.y)








