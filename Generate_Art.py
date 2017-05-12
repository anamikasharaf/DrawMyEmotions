_author__ = 'anamika.sharaf'

from turtle import *
from random import randint
from random import *
from Tkinter import *
import glob, os, pdb
from PIL import Image

#for stars
def random_star_color(emotion_num):
	if(emotion_num == 1):
		random_color = ["hotpink", "MediumVioletRed"]
		color = choice(random_color)
	if(emotion_num == 2):
		random_color = ["slategray", "black","darkslategray"]
		color = choice(random_color)
	if(emotion_num == 3):
		random_color = ["gainsboro", "saddlebrown"]
		color = choice(random_color)
	if(emotion_num == 4):
		random_color = ["Indigo", "midnightblue"]
		color = choice(random_color)
	if(emotion_num == 5):
		random_color = ["LightCoral", "DarkSalmon"]
		color = choice(random_color)
	return color

#for circle and splatter
def random_dot_color(emotion_num):
	if(emotion_num == 1):
		random_color = ["MediumVioletRed","lightcoral","hotpink","palevioletred"]
		color = choice(random_color)
	if(emotion_num == 2):
		random_color = ["slategray","darkslategray","black"]
		color = choice(random_color)
	if(emotion_num == 3):
		random_color = ["darkgoldenrod","tan","brown"]
		color = choice(random_color)
	if(emotion_num == 4):
		random_color = ["navy","RoyalBlue"]
		color = choice(random_color)
	if(emotion_num == 5):
		random_color = ["LightCoral","Red","Maroon"]
		color = choice(random_color)
	if(emotion_num == 6):
		random_color = ["yellowgreen","seagreen"]
		color = choice(random_color)
	return color

#for foreground shapes
def foreground_color(emotion_num):
	if(emotion_num == 1):
		random_color = ["lightsalmon","coral", "MediumVioletRed", "palevioletred","orange"]
		color = choice(random_color)
	if(emotion_num == 2):
		random_color = ["black","dimgray"]
		color = choice(random_color)
	if(emotion_num == 3):
		random_color = ["rosybrown", "goldenrod", "brown"]
		color = choice(random_color)
	if(emotion_num == 4):
		random_color = ["darkmagenta", "DarkSlateBlue", "DarkRed","MidnightBlue"]
		color = choice(random_color)
	if(emotion_num == 5):
		random_color = ["Red", "DarkRed","IndianRed","firebrick","orangered"]
		color = choice(random_color)
	if(emotion_num == 6):
		random_color = ["darkolivegreen","darkgoldenrod","darkslategray","forestgreen"]
		color = choice(random_color)
	return color

# random quadrant selection
def random_place(random_qadrant):
	penup()
	if(random_qadrant == 1):
		x = randint(-400,400)
		y = randint(0,400)
	if(random_qadrant == 2):
		x = randint(-400,0)
		y = randint(-400,400)
	if(random_qadrant == 3):
		x = randint(-400,400)
		y = randint(-400,0)
	if(random_qadrant == 4):
		x = randint(0,400)
		y = randint(-400,400)
	if(random_qadrant == 5):
		x = randint(-400,400)
		y = randint(-400,400)
	goto(x,y)
	pendown()

#choose quadarant for dots
def choose_quant(random_qadrant):
	if(random_qadrant == 1):
		quadrant_alternative = 2
	if(random_qadrant == 2):
		quadrant_alternative = 3
	if(random_qadrant == 3):
		quadrant_alternative = 4
	if(random_qadrant == 4):
		quadrant_alternative = 1
	if(random_qadrant == 5):
		quadrant_alternative = 5
	return quadrant_alternative

#drawing circles
def draw_circle(emotion_num,random_qadrant):
	color_picked = foreground_color(emotion_num)
	random_place(random_qadrant)
	hideturtle()
	radius = randint(70,100)
	begin_fill()
	color(color_picked)
	dot(radius)
	end_fill()

#drawing ellipse
def draw_ellipse(emotion_num,random_qadrant):
	radius1 = randint(3,10)
	radius2 = randint(5,15)
	color_picked = foreground_color(emotion_num)
	random_place(random_qadrant)
	shape("circle")
	shapesize(radius1,radius2)
	pencolor(color_picked)
	fillcolor(color_picked)
	stamp()

#drawing dots
def draw_dots(emotion_num,size,random_qadrant):
	if(size == 0):
		radius = randint(20,30)
	if(size == 1):
		radius = randint(6,10)
	if(size == 2):
		radius = randint(8,15)
	random_place(random_qadrant)
	color_picked = random_dot_color(emotion_num)
	hideturtle()
	begin_fill()
	color(color_picked)
	dot(radius)
	end_fill()

#drawing hollow circles
def draw_hollow_circle(emotion_num,random_qadrant):
	random_place(random_qadrant)
	radius = randint(20,40)
	penup()
	color_picked = random_dot_color(emotion_num)
	pencolor(color_picked)
	width(10)
	pendown()
	setheading(180)
	circle(radius)
	penup()

#drawing stars
def draw_star(emotion_num,random_qadrant):
	size = randint(5,15)
	angle = 120
	color_picked = random_star_color(emotion_num)
	fillcolor(color_picked)
	random_place(random_qadrant)
	hideturtle()
	begin_fill()
	pencolor(color_picked)
	for side in range(5):
	    forward(size)
	    right(angle)
	    forward(size)
	    right(72 - angle)
	end_fill()

#draw rectangle
def draw_rectangle(emotion_num,size,random_qadrant):
	random_place(random_qadrant)
	hideturtle()
	if(size == 1):
		length = randint(150,250)
		height = randint(150,250)
		color_picked = foreground_color(emotion_num)
	if(size == 2):
		length = randint(100,150)
		height = randint(100,150)
		color_picked = foreground_color(emotion_num)
	if(size == 3):
		length = randint(10,20)
		height = randint(10,20)
		color_picked = random_dot_color(emotion_num)
	begin_fill()
	color(color_picked)
	forward(length)
	right(90)
	forward(height)
	right(90)
	forward(length)
	right(90)
	forward(height)
	right(90)
	end_fill()

#draw polygons based on number of dots 
def sprinkle(emotion_num,random_quadrant):
	hideturtle()
	color_picked = random_dot_color(emotion_num)
	begin_fill()
	color(color_picked)
	for i in range(5):
		random_place(random_quadrant)
		dot(4)
	end_fill()

#generate happy art
def generate_happy_art():

	emotion_num = 1
	background_color = "hotpink" 
	bgcolor(background_color)
	setup( width = 500, height = 500)

	random_quadrant = randint(1,4)
	alternative = choose_quant(random_quadrant)
	for i in range(60):
		if (i%2 == 0):
			draw_ellipse(emotion_num,random_quadrant)
		draw_circle(emotion_num,random_quadrant)
 		draw_hollow_circle(emotion_num,random_quadrant)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	for i in range(200):
		draw_dots(emotion_num,1,alternative)
	for i in range(10):
		draw_star(emotion_num,random_quadrant)
	for i in range(200):
		draw_dots(emotion_num,2,5)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	convert_file(background_color,0.8)

#generate sad art
def generate_sad_art():

	emotion_num = 2
	background_color = "gray"
	bgcolor(background_color)
	setup( width = 500, height = 500)

	random_quadrant = randint(1,4)
	alternative = choose_quant(random_quadrant)
	
	for i in range(10):
		sprinkle(emotion_num,5)
	for i in range(60): 
		if (i%2 == 0):
			draw_ellipse(emotion_num,random_quadrant)
		draw_circle(emotion_num,random_quadrant)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	for i in range(200):
		draw_dots(emotion_num,1,alternative)
	for i in range(200):
		draw_dots(emotion_num,2,5)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	convert_file(background_color,0.8)

#generate neutral art
def generate_neutral_art():

	emotion_num = 3
	background_color = "peru"
	bgcolor(background_color)
	setup( width = 500, height = 500)

	random_quadrant = randint(1,4)
	alternative = choose_quant(random_quadrant)

	for i in range(60):
		if (i%2 == 0):
			draw_ellipse(emotion_num,random_quadrant)
		draw_circle(emotion_num,random_quadrant)
		draw_hollow_circle(emotion_num,random_quadrant)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	for i in range(200):
		draw_dots(emotion_num,1,alternative)
	for i in range(200):
		draw_dots(emotion_num,2,5)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	convert_file(background_color,0.5)

#generate fear art
def generate_fear_art():
	emotion_num = 4
	background_color = "Slateblue"
	bgcolor(background_color)
	setup( width = 500, height = 500)

	random_quadrant = randint(1,4)
	alternative = choose_quant(random_quadrant)

	for i in range(10):
		sprinkle(emotion_num,5)
	for i in range(60):
		if (i%2 == 0):
			draw_ellipse(emotion_num,random_quadrant)
		draw_circle(emotion_num,random_quadrant)
		draw_hollow_circle(emotion_num,random_quadrant)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	for i in range(200):
		draw_dots(emotion_num,1,alternative)
	for i in range(200):
		draw_dots(emotion_num,2,5)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	convert_file(background_color,0.5)

#generate anger art
def generate_anger_art():
	emotion_num = 5
	background_color = "brown"
	bgcolor(background_color)
	setup( width = 500, height = 500)

	random_quadrant = randint(1,4)
	alternative = choose_quant(random_quadrant)

	for i in range(10):
		sprinkle(emotion_num,5)
	for i in range(60):
		if (i%2 == 0):
			draw_ellipse(emotion_num,random_quadrant)
		draw_circle(emotion_num,random_quadrant)
		draw_hollow_circle(emotion_num,random_quadrant)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	for i in range(200):
		draw_dots(emotion_num,1,alternative)
	for i in range(200):
		draw_dots(emotion_num,2,5)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	convert_file(background_color,0.5)

#generate disgust art
def generate_disgust_art():
	emotion_num = 6
	background_color = "limegreen"
	bgcolor(background_color)
	setup( width = 500, height = 500)

	random_quadrant = randint(1,4)
	alternative = choose_quant(random_quadrant)

	for i in range(10):
		sprinkle(emotion_num,5)
	for i in range(60):
		if (i%2 == 0):
			draw_ellipse(emotion_num,random_quadrant)
		draw_circle(emotion_num,random_quadrant)
		draw_hollow_circle(emotion_num,random_quadrant)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	for i in range(200):
		draw_dots(emotion_num,1,alternative)
	for i in range(200):
		draw_dots(emotion_num,2,5)
	for i in range(100):
		draw_dots(emotion_num,0,alternative)
	convert_file(background_color,0.7)

def convert_file(background_color, alpha):
	#save the turtle module in .eps images
	ts = getscreen()
	ts.getcanvas().postscript(file="foreground.eps")

	#convert .eps file to .png
	openFiles = glob.glob('*.eps')
	for files in openFiles:
		inFile = Image.open(files)
		fileName = os.path.splitext(files)[0] # gets filename
		image2 = Image.open(fileName + ".eps")
		image2.save(fileName+".png","png", quality = 1000)

	#blending two images
	image1 = Image.new("RGB", (500,500), background_color)
	image1.save("background.png", "png", quality = 1000)
	image3 = Image.blend(image1,image2,alpha)
	image3.save("final_image.png","png", quality = 1000)

