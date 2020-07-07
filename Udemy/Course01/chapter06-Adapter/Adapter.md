# Adapter

### Definition
An adapter is a construct that help you make the interface you need, than the interface you have. It's a construct which adapts an existing interface X to conform to the required interface Y.

### Explanation
Suppose you have an API that does someting specific. Now you want to use that API for some other thing. But you can't do that, right?

For example: you have an API that draws points

```
class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

def draw_point(p):
    print('.', end='')
```

Now lets say have a line and you want to draw rectangle with the lines using the **draw_point** API. Here is the Line and Rectangle

```
class Line:
    def __init__(self, start, end):
        self.end = end
        self.start = start


class Rectangle(list):
    """ Represented as a list of lines. """

    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))
```

So, our draw api can't draw rectangles because it can only draw points. So what can we do?

We can introduce an Adapter which will adapt our Rectangles to points for teh draw api to work.

Here us our adapter:

```
class LineToPointAdapter(list):
    count = 0

    def __init__(self, line):
        self.count += 1
        print(f'{self.count}: Generating points for line '
              f'[{line.start.x},{line.start.y}]→'
              f'[{line.end.x},{line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))

```

Now we can draw rectangles using the draw_points api.


```
def draw(rcs):
    print("\n\n--- Drawing some stuff ---\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)

if __name__ == '__main__':
    rs = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6)
    ]
    draw(rs)
    draw(rs)
```

So, there is our adapter.

But there is one problem we need to think about. Each time we use the adapter, on the same class it will translate Rantanle to point anew, no matter they are the same or not. It's a waste of time and resource.

To make it better we can cache results of Adapter. If changes already exist we return from cache and if not we make changes and cache the them like we do it `with_caching.py` file.

