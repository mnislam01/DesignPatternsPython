# Circles and squares
# Each can be rendered in vector or raster form
"""
Lets say you Have a Circle and Square
you want to draw them.
How do you provide nice draw API so that circles and squares are rendered?

The images can be either Vector or Raster. How do you handle that without making it complex?
"""

from abc import ABC

# Lets make an abstract renderer class first
class Renderer(ABC):
    def render_circle(self, radius):
        pass

# Now lets make Renderers now

# Make a Vector Renderer
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')

# Make a Make a Raster Renderer
class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for circle of radius {radius}')


# Both are inheriting the Abstract renderer


# Now, lets make and Abstract shape
class Shape(ABC):
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self): pass
    def resize(self, factor): pass


# Since cirlces and Squares are shape they can inherit the abstract class
class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


if __name__ == '__main__':
    raster = RasterRenderer() # We have a raster randerer
    vector = VectorRenderer() # we have a vector renderer
    circle = Circle(vector, 5) # To draw the circle with a renderer only we have to pass the rendered
    circle.draw() # with nice draw api from circle we can now draw the shape
    circle.resize(2)
    circle.draw()