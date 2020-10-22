"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

With the help of babynames.py, this program produces a canvas
that user can input someone's name even as many keys in the same time.
These information are showed in the form of line graph.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    each_width = (width-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    x_coordinate = year_index*each_width + GRAPH_MARGIN_SIZE
    return x_coordinate



def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i),
                           CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    color_num = 0
    unit = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000
    # We need to define the distance of per rank in one canvas, including 1000 ranks.
    for lookup_name in lookup_names:
        # Maybe user will input many names to search
        count = 0
        # This count helps us record the order.
        color_num += 1
        # This color_num helps us recorded the order
        for year in YEARS:
            count += 1
            if str(year) not in name_data[lookup_name]:
                # Global YEARS is a figure list
                if year == YEARS[0]:
                    # the first rank does not need to create line with the previous one
                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, count - 1),
                                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=(f'{lookup_name} *'),
                                       anchor=tkinter.SW, fill=COLORS[(color_num - 1) % len(COLORS)])
                else:
                    # Except for the first year, every rank of year should be draw with previous one.
                    if str(year-10) not in name_data[lookup_name]:
                # If the previous rank is out of 1000, which y coordinate is still CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, count - 2),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, count - 1),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           fill=COLORS[(color_num - 1) % len(COLORS)])
                    else:
                # if the previous rank is a fixed number we can calculate its y coordinate
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, count - 2),
                                           int(name_data[lookup_name][str(year - 10)])*unit + GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, count - 1),
                                           CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                           fill=COLORS[(color_num - 1) % len(COLORS)])

                    canvas.create_text(get_x_coordinate(CANVAS_WIDTH, count - 1),
                                      CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                       text=(f'{lookup_name} *'),
                                       anchor=tkinter.SW, fill=COLORS[(color_num - 1) % len(COLORS)])
            elif int(name_data[lookup_name][str(year)]) <= 1000:
                if year != YEARS[0]:
                    if str(year - 10) not in name_data[lookup_name]:
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, count - 2),
                                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, count - 1),
                                           int(name_data[lookup_name][str(year)])*unit + GRAPH_MARGIN_SIZE,
                                           fill=COLORS[(color_num - 1) % len(COLORS)])
                    else:
                        # the first rank does not need to create line with the previous one
                        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, count - 2),
                                           int(name_data[lookup_name][str(year - 10)])*unit + GRAPH_MARGIN_SIZE,
                                           get_x_coordinate(CANVAS_WIDTH, count - 1),
                                           int(name_data[lookup_name][str(year)])*unit + GRAPH_MARGIN_SIZE,
                                           fill=COLORS[(color_num - 1) % len(COLORS)])

                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, count-1),
                                   int(name_data[lookup_name][str(year)])*unit-TEXT_DX+GRAPH_MARGIN_SIZE,
                                   text=(f'{lookup_name}{name_data[lookup_name][str(year)]}'),
                                   anchor=tkinter.SW, fill=COLORS[(color_num-1)%len(COLORS)])





# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)
    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
