"""
picture.py
Author: Esther Hacker
Credit: N/A

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/

# Three primary colors with no transparency (alpha = 1.0)
white = Color(0xfffff0, 1.0)
white2 = Color(0xf8f8ff, 1.0)
red = Color(0xff0000, 1.0)
red2 = Color(0xff0000, 0.5)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
yellow = Color(0xffff00	, 1.0)
yellow2 = Color(0xe9e900, 0.3)
brown = Color(0x8b4513, 1.0)
gray = Color(0xd3d3d3, 1.0)
dark_gray = Color(0x708090, 1.0)
light_blue = Color(0x6495ed, 0.2)
green = Color(0x006400, 1.0)

# Define a line style that is a thin (1 pixel) wide black line
thinline = LineStyle(1, black)
# A graphics asset that represents a rectangle

#window
window = RectangleAsset(50, 50, thinline, white)
window2 = RectangleAsset(50, 50, thinline, white)
window3 = RectangleAsset(50, 50, thinline, white)
window4 = RectangleAsset(50, 50, thinline, white)
windowpane = RectangleAsset(50, 50, thinline, yellow2)
windowpane2 = RectangleAsset(50, 50, thinline, yellow2)
windowpane3 = RectangleAsset(50, 50, thinline, yellow2)
windowpane4 = RectangleAsset(50, 50, thinline, yellow2)
windowframe = RectangleAsset(60, 60, thinline, brown)
windowframe2 = RectangleAsset(60, 60, thinline, brown)
windowframe3 = RectangleAsset(60, 60, thinline, brown)
windowframe4 = RectangleAsset(60, 60, thinline, brown)

#Sky
sky = RectangleAsset(1000, 1000, thinline, light_blue)

#Ground
ground = RectangleAsset(1000, 1000, thinline, green)

#Main square of the house
house = RectangleAsset(300, 300, thinline, gray)

#Roof
roof = PolygonAsset ([(0, 100), (200, 0), (400, 100), (0, 100)], thinline, dark_gray)

#sun
sun = CircleAsset (70, thinline, yellow)

#door
door = RectangleAsset(76, 140, thinline, brown)

#Doorknob
doorknob = EllipseAsset(8, 5, thinline, white2)

#door trim
doortrim = RectangleAsset(300, 15, thinline, white)

#Sprites
Sprite(sky)
Sprite(ground, (0, 200))
Sprite(house, (250, 150))
Sprite(roof, (200, 50))
Sprite(sun)
Sprite(doortrim, (250, 435))
Sprite(door, (362, 310))
Sprite(doorknob, (415, 370))

#Window 1
Sprite(windowframe, (295, 195))
Sprite(window, (300, 200))
Sprite(windowpane, (300, 200))

#Window 2
Sprite(windowframe2, (445, 195))
Sprite(window2, (450, 200))
Sprite(windowpane2, (450, 200))

#Window 3
Sprite(windowframe3, (445, 325))
Sprite(window3, (450, 330))
Sprite(windowpane3, (450, 330))

#Window 4
Sprite(windowframe4, (295, 325))
Sprite(window4, (300, 330))
Sprite(windowpane4, (300, 330))

# add your code here /\  /\  /\


myapp = App()
myapp.run()
