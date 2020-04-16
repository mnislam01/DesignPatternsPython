# Factory Method

The idea of Factory method is, instead of making a large initializer of an object, we can provide meaning and convenient methods which will make objects the kind we need.


For example, if we need to a define Coordination. So, object we could do the following:

```
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

By the look of it we know it's a Cartesian coordination. What if we need Polar Coordination? Well, we can do that too like following:

```
from enum import Enum
from math import *


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2

class Coordinate:
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = a * cos(b)

```

We created a massive constructor that we don't want. From the builder pattern we learned we don't like massive constructors like that. 

So, what we can do here?

Well, we can this

```
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class CoordinateFactory:
    @staticmethod
    def new_cartesian_coordinate(x, y):
        return Coordinate(x, y)

    @staticmethod
    def new_polar_coordinate(rho, theta):
        return Coordinate(rho * sin(theta), rho * cos(theta))

```

We we can use them like

```
p1 = PointFactory.new_cartesian_coordinate(1, 2)
print(p1)
p2 = PointFactory.new_polar_coordinate(1, 2)
print(p2)
```

