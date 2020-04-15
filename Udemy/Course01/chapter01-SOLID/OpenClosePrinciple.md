Open close principle states that a class in only open for **Extention** but closed for **Modification**.

Means, we need to design featuers in sush a way that, if we need to extend it or add new functionality to that, we do that by doing only Extension. Do would not modify the original class.


For exampple: let's say we need a filter feature in our application by which we would filter products by color, size etc.

So what we would do is, we write a class called filter and implement two methods **filter_by_color** and **filter_by_size**

```
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color: yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size: yield p
```

And now, if we need to add another enhancement, lets say, **filter_by_color_and_size**, We would have to add another method in Filter class to do that.


That's violated the **Open-Close Principle**. We would not modify the **Filter** class.

Rather we need to desing the classes and their responsibilites in such a way that we do not need to modify it. We will enhance it's functionality using inheritance featuer of OOP.


So, we need to design the the **Filter** class differently, like this:


```
class Filter(object):

    def filter(self, products, spec):
        pass



class NewFilter(Filter):

    def filter(self, products, spec):
        for p in products:
            if spec.is_satisfied(p):
                yeild p

```


Now we have introduced a New pattern here called Specification pattern. To make the filter work we need a Specification class.


```
class Specification:
    def is_satisfied(self, p):
        pass



class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, p):
        return p.color == self.color


new_filter = NewFilter()

color = ColorSpecification('GREEN')

new_filter.filter(products, color)

```


Now if we need to add a new filter we don't need to change or modify Filter or Specification. We will have to add a new 

Specification And using it, we will be able to filter Products.




