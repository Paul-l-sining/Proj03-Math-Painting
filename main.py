from shape import Rectangle, Square
from canvas import Canvas

# Building CLI interface
print('Hey user, welcome to math painting tool')
print('To start with, we need to create a canvas')

# make canvas
width = int(input('Please enter canvas width: '))
height = int(input('Please enter canvas height: '))
c_color = input('Enter canvas color (white or black): ')
color = {'white': [255, 255, 255],'black':[0, 0, 0]}
c = Canvas(a=height, b=width, color=color[c_color])

# draw shape
while True:
    shape = input('What do you like to draw? (rectangle or square) Enter quit to quit. ')
    print(f'Now please enter the left top coordinate (x, y) of the {shape} ')

    # config a rectangle
    if shape.lower() == 'rectangle':
        x = int(input('Enter x of the rectangle: '))
        y = int(input('Enter y of the rectangle: '))
        w = int(input('Enter the width of the rectangle: ')) # rectangle width
        h = int(input('Enter the height of the rectangle: ')) # rectangle height
        r = int(input('How much red do you want the rectangle to have? (0~255)'))
        g = int(input('How much green? '))
        b = int(input('How much blue? '))
        rec = Rectangle(x=x, y=y, a=w, b=h, color=[r, g, b])
        rec.draw(c)

    # config a square
    elif shape.lower() == 'square':
        x = int(input('Enter x of the square: '))
        y = int(input('Enter y of the square: '))
        l = int(input('Enter the length of the square: '))
        r = int(input('How much red do you want the square to have? (0~255)'))
        g = int(input('How much green? '))
        b = int(input('How much blue? '))
        sqr = Square(x=x, y=y, a=l, color=[r, g, b])
        sqr.draw(c)
    elif shape.lower() == 'quit':
        break
    else:
        print('Invalid input, try again please. ')

c.make('canvas.png')


# # without CLI testing
# c = Canvas(a=700, b=1000, color=[255, 255, 0])
# r = Rectangle(x=200, y=100, a=600, b=100, color=[225, 66, 55])
# r.draw(c)
# s = Square(x=400, y=200, a=200, color=[23, 12, 200])
# s.draw(c)
# r = Rectangle(x=200, y=400, a=600, b=100, color=[225, 66, 55])
# r.draw(c)
# c.make('canvas_2.0.png')