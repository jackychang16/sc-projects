"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

This program helps user to restore the background without people by image processing
of many photos.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_distance = ((pixel.red-red)**2 + (pixel.green-green)**2 + (pixel.blue-blue)**2)**0.5
    # ** 0.5 = square root
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    total_red = 0
    total_blue = 0
    total_green = 0
    for pixel in pixels:
        total_red += pixel.red
        total_green += pixel.green
        total_blue += pixel.blue

    avg_red = total_red // len(pixels)
    avg_blue = total_blue // len(pixels)
    avg_green = total_green//len(pixels)
    avg_color = []
    # we can only put many information in one list
    avg_color.append(avg_red)
    avg_color.append(avg_green)
    avg_color.append(avg_blue)
    return avg_color


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg = get_average(pixels)
    new_color_distance = get_pixel_dist(pixels[0],avg[0],avg[1],avg[2])
    # we calculate color_distance of the first pixel and make it as new_color_distance momentarily.
    best_pixel = pixels[0]
    # the first pixel

    for pixel in pixels:
        color_distance = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        if new_color_distance > color_distance:
            new_color_distance = color_distance
            best_pixel = pixel
            # if we calculate a smaller value of new_color_distance,we should renew this one and record this pixel
            # (pixel.red,pixel.green,pixel.blue)
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    for x in range (width):
        for y in range (height):
            pixels = []
        # we should create a list out of next loop because this list record because of every pixel in the same position
            for image in images:
                pixel = image.get_pixel(x,y)
                pixels.append(pixel)
            # we get every pixel in the same position from different photos as well as compare which one is the best
            # pixel we need to record and paste to the result.
            best_pixel = get_best_pixel(pixels)
            final_pixel = result.get_pixel(x,y)
            final_pixel.red = best_pixel.red
            final_pixel.blue = best_pixel.blue
            final_pixel.green = best_pixel.green


    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    # green_pixel = SimpleImage.blank(20,20, "green").get_pixel(0,0)
    # red_pixel = SimpleImage.blank(20,20,'red').get_pixel(0,0)
    # blue_pixel = SimpleImage.blank(20,20,'blue').get_pixel(0,0)
    # best1 = get_best_pixel([green_pixel,blue_pixel,blue_pixel])
    # print(best1.red,best1.green,best1.blue)
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
