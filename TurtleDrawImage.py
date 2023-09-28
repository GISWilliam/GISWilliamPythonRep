from PIL import Image
import turtle
import numpy as np

# Function to convert RGBA color to hexadecimal color
def rgba_to_hex(rgba):
    r, g, b, a = rgba
    r, g, b = int(r), int(g), int(b)
    return f'#{r:02X}{g:02X}{b:02X}'

# Function to draw a pixel at the specified coordinates with the given color
def draw_pixel(x, y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor(color)
    print(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(1)
        turtle.right(90)
    turtle.end_fill()

# Load an image using Pillow
image_path = r'Desktop\rockface.png'  # Replace with the path to your image
image = Image.open(image_path)

# Convert the image to RGBA mode to handle the alpha channel
image = image.convert("RGBA")

# Get the RGBA values of each pixel as a NumPy array
pixel_data = np.array(image)

# Create a Turtle screen
screen = turtle.Screen()
screen.title("Pixel Art")

# Set up the Turtle environment
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("white")

# Set the scaling factor for the drawing
scaling_factor = 1

# Iterate through each pixel and draw it on the screen
height, width, _ = pixel_data.shape
for y in range(height):
    for x in range(width):
        rgba = pixel_data[y, x]
        turtle_x = x - (width // 2)
        turtle_y = (height // 2) - y
        turtle_x *= scaling_factor
        turtle_y *= scaling_factor
        color_hex = rgba_to_hex(rgba)
        draw_pixel(turtle_x, turtle_y, color_hex)

# Close the Turtle graphics window when clicked
screen.exitonclick()
