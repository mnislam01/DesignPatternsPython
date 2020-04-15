Liscov Substitution Principle says that, if we Use a class (A) in somewhere, then we should be able to substitute that class (A) with another class (B) which has inhereted class (A). And it shouldn't break the principle of class (A) when we are using Class (B) in place of Class (A)


for example, lets say we make a class **Rectangle**. 

```
class Rectangle(object):
    def __init__(self, a, b):
        self.height = a
        self.width = b

    def area(self):
        return self.height * self.width
```


We are using it by calling it's area like below:

```
ractangle = Rectangle(3, 4)

def show_area(ract):
    print(ract.area())


show_area(ractangle)
```


Now, lets say we make another class called **Square**. Basicly squares are all Ractangles by nature. But it's height and lengths are same.


```
class Square(Rectangle):
    def __init__(a):
        super().__init__(a,a)

```


And lets use both of them

```
square = Square(2)

show_area(square)

```

Using **Square** and replacing it in such a way that, we are not breaking other code where **Ractangle** is used.

