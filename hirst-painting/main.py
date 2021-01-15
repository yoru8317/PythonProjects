
# Extracting the colors from image
# import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as t
import random

t.colormode(255)
arrow = t.Turtle()
arrow.penup()
arrow.speed("fastest")
arrow.hideturtle()
color_list = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48),
              (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70),
              (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71),
              (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48),
              (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56)]

arrow.setheading(225)
arrow.forward(300)
arrow.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    arrow.dot(20, random.choice(color_list))
    arrow.forward(50)

    if dot_count % 10 == 0:
        arrow.setheading(90)
        arrow.forward(50)
        arrow.setheading(180)
        arrow.forward(500)
        arrow.setheading(0)



screen = t.Screen()
screen.exitonclick()


