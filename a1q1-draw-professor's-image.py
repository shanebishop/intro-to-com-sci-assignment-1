#
# Shane Bishop
# 101030053
#
# Reference List:
# Gaddis, T. (2015). "Starting Out With Python"
# Tutorial 1: Drawing with the SimpleGraphics Library. (2016-09-19). Retrieved from https://culearn.carleton.ca/moodle/pluginfile.php/1832043/mod_resource/content/1/COMP1405-F16-XXX-XX-%28Simple%20Graphics%20Tutorial%20-%20Part%201%20of%202%29.pdf.
# Tutorial 2: Using Images with the SimpleGraphics Library. (2016-09-19). Retrieved from https://culearn.carleton.ca/moodle/pluginfile.php/1832053/mod_resource/content/1/COMP1405-F16-XXX-XX-%28Simple%20Graphics%20Tutorial%20-%20Part%202%20of%202%29.pdf.
#

# Import SimpleGraphics
from SimpleGraphics import *

# Draw white background
setOutline("")
rect(0, 0, 100, 50)
setFill(225, 225, 225)

# Draw black polygon
setOutline("")
setFill(0, 0, 0)
polygon(59, 0, 88, 0, 88, 49, 29, 49, 29, 7, 59, 7)

# Draw blue polygon
setOutline("")
setFill(0, 0, 102)
polygon(37, 15, 51, 15, 57, 23, 52, 49, 37, 49)

# Draw first semi-transparent polygon
setOutline("")
setFill(51, 51, 51)
polygon(44, 22, 59, 22, 73, 38, 73, 46, 71, 49, 44, 49)

# Draw second semi-transparent polygon
setOutline("")
setFill(51, 51, 102)
polygon(44, 22, 56, 22, 57, 25, 52, 49, 44, 49)