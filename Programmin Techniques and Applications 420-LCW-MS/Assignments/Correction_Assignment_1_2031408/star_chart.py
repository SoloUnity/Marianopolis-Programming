# Gordon Ng, 2031408
# R. Vincent , instructor
# Advanced Programming , section 1 
# Assignment 1, Exercise 1


# 20/20 very good
#
# Warnings:
#  ** Don't import unneeded things!
#  ** Use maxsplit=5, not maxsplit=6. You are actually reading a few names
#     incorrectly (I think).

# A few notes:
# - There are 4428 stars in stars.txt
# - Of these, 229 have one or more names associated with them.
# - Only 11 stars have two names
# - Two names are repeated, Boo_Kappa and Boo_Zeta, so there
#   are only 227 uniquely named stars.

from multiprocessing.sharedctypes import Value
from re import X
import math
             

# Assignment code below
# BASIC TKINTER INITIALIZATION

import tkinter as tk
SIZE = 1000                     # Use this named constant!
color = "#FFFFFF"               # Colour chosen
wnd = tk.Tk()
canvas = tk.Canvas(wnd, width=SIZE, height=SIZE, background='black')
canvas.pack()
wnd.title('Star chart')

# DO NOT CHANGE ANYTHING BELOW THIS LINE!

def draw_line(x0, y0, x1, y1, color):
    '''Draw a line connecting two points, given integer coordinates for the
    start position (x0, y0) and end position (x1, y1). The color is a string, 
    either a color name (e.g. 'red') or an RGB value '#RRGGBB'.'''
    canvas.create_line(x0, y0, x1, y1, width=1, fill=color)

def draw_star(x, y, radius, color):
    '''Draw a star as a filled circle with a given center (in pixel
    coordinates), radius (in pixels), and color (as above).'''
    if radius < 1:
        canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill=color, width=1)
    else:
        canvas.create_oval(x - radius,
                           y - radius,
                           x + radius,
                           y + radius,fill=color, width=0)

# Assignment Code here                     
def coords_to_pixel(star_x, star_y, size):
    """
    star_x is a float representing the x star coordinate
    star_y is a float representing the y star coordinate
    Function serves to translate star coordinates to pixel coordinates
    """
    star_x = float(star_x)    # Converts string values to float values
    star_y = float(star_y)
    middle = size // 2
    if star_x >= -1 and star_x <= 1 and star_y >= -1 and star_y <= 1:
        return (middle + (star_x * middle), middle - (star_y * middle)) #Returns converted pixel coordinates

def read_stars(fp):
    """
    fp is an opened file containing stars
    Function returns a tuple of (star coordinates dictionary, a magnitude dictionary and a names dictionary)
    """
    starCoordinatesDict = {}
    magnitudeDict = {}
    namesDict = {}
    for line in fp:
        tempData = line.split(maxsplit = 6)                 
        starCoordinatesDict[tempData[1]] = (tempData[3] , tempData[2])                              # Draper key, xy coordinates value, adding to the starCoordinates dictionary
        magnitudeDict[tempData[1]] = tempData[4]                                                    # Draper key, magnitude value, adding to the magnitude dictionary
        if len(tempData) == 6:
            for name in tempData[5].strip().split(","):
                namesDict[name.strip().replace("_", " ").upper()] = tempData[1]                     # Star name key, Draper value, adding to the name dictionary
    return (starCoordinatesDict, magnitudeDict, namesDict)

def plot_by_magnitude(size, coords, magnitudes):
    """
    size is an integer representing the desired drawn canvas
    coords is a dictionary of star coordinates
    magnitudes is a dictionary of star magnitudes 
    function plots/draws stars based on their magnitude
    """
    for key in coords.keys():
        coordinates = coords_to_pixel(coords[key][0], coords[key][1], size)                         # Converting star coords to pixel coords
        draw_star(coordinates[0], coordinates[1], math.log(8 - float(magnitudes[key])), color)      # Draws the stars on the canvas based on magnitude 

def read_constellation_lines(fp):
    """
    fp is an opened files containing stars of a constellation
    function returns a dictionary of the constellation
    """
    tempDict = {}
    tempList = []
    for line in fp:
        tempData = line.strip().split(",")  
        tempList.append(tempData[0])
        tempList.append(tempData[1])
    tempDict[tempList[0]] = tempList
    return tempDict

def plot_constellation(coords, lines, names, color, size):
    """
    coords is a dictionary of star coordinates
    lines is a dictionary of constellation stars
    color is a string representing the color of the lines
    size is an integer representing the size of the desired canvas
    function plots/draws constellation lines
    """
    for stars in lines.values():
        for i in range(0, len(stars), 2):
            star1 = stars[i].strip()   # First star of the drawn line
            star2 = stars[i+1].strip() # Second star of the drawn line
            if not star1.isdigit():    # Converts star names to its draper number                             
                star1 = names[star1]
            if not star2.isdigit():
                star2 = names[star2]
            coords1 = coords_to_pixel(coords[star1][0], coords[star1][1], size) # Converts a stars coordinates to pixel coordinates
            coords2 = coords_to_pixel(coords[star2][0], coords[star2][1], size)
            draw_line(coords1[0], coords1[1], coords2[0], coords2[1], color)    # Draws lines from pixel coordinates
           

# ADD YOUR CODE ABOVE THIS LINE

# THE MAIN PROGRAM IS HERE (DO NOT CHANGE THIS)!

constellation_files = [
    ('Cas_lines.txt', 'white'),
    ('Cyg_lines.txt', 'white'),
    ('BigDipper_lines.txt', 'white'),
    ('Bootes_lines.txt', 'white'),
    ('UrsaMinor_lines.txt', 'white'),
    ('Cepheus_lines.txt', 'white'),
    ('Draco_lines.txt', 'white'),
    ('Auriga_lines.txt', 'white')
]

fp = open('stars.txt')
coords, magnitudes, names = read_stars(fp)
assert len(coords) == len(magnitudes)
print("Read", len(coords), "star coordinates and magnitudes")
print("Read", len(names), "unique star names referring to ", len(set(names.values())), "distinct stars")
fp.close()
plot_by_magnitude(SIZE, coords, magnitudes)
for fname, color in constellation_files:
    fp = open(fname)
    lines = read_constellation_lines(fp)
    fp.close()
    plot_constellation(coords, lines, names, color, SIZE)

# DO NOT DELETE THIS LINE!
wnd.mainloop()


