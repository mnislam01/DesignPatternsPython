# Motivation to use Builder Pattern

We know some objects are simple and can be created in a simple initializer. But some are more complicated objects require more ceremony to create. So, having an object with 10 initializer arguments is not productive. 

Instead, we opt for piecewise construction. So what happens is that we call different methods to initialize of a special component called **Builder** which actually initialize the object.

**Builder**, provides API's for constructing the object step by step.


So, we can conslude with the definition below:

```
When piecewise object construction is complicated, prodive and API for for doing it succinctly.
```

# Builder Design Pattern

Why do we need it?
```
Okay, so builder is required when you have some sort of complication object to construct. So, not just constructing an object in a single statement, intead doing it step by step.
```


Let's say we want to build html paragraphs. So we wrote 

```
hello = 'hello'
parts = ['<p>', hello, '</p>']
print(''.join(parts))
```

It build paragraphs like

```
<p>hello</p>
```

But if we want to make complicated elements, lets say, with nested elements. Things also get complicated.

```
words = ['hello', 'world']
parts = ['<ul>']
for w in words:
    parts.append(f'  <li>{w}</li>')
parts.append('</ul>')
print('\n'.join(parts))


**Output**
<ul>
    <li>hello</li>
    <li>world</li>
</ul>
```

What if someone forget's to put to close the element? What is more nested elements come?

To solve this kind of problem we can think it different way. We can build an object called Element.

```
class HtmlElement:
    indent_size = 2

    def __init__(self, name="", text=""):
        self.name = name
        self.text = text
        self.elements = []

    def __str(self, indent):
        lines = []
        i = ' ' * (indent * self.indent_size)
        lines.append(f'{i}<{self.name}>')

        if self.text:
            i1 = ' ' * ((indent + 1) * self.indent_size)
            lines.append(f'{i1}{self.text}')

        for e in self.elements:
            lines.append(e.__str(indent + 1))

        lines.append(f'{i}</{self.name}>')
        return '\n'.join(lines)

    def __str__(self):
        return self.__str(0)
```

Then use a **Builder** object to build elemnts using *builder API's*.

```
class HtmlBuilder:
    __root = HtmlElement()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.name = root_name

    def add_child(self, child_name, child_text):
        self.__root.elements.append(
            HtmlElement(child_name, child_text)
        )
```

For example:

```
html = HtmlElement.create('ul')
html.add_child('li', 'hello')
html.add_child('li', 'world')
print(html)
```


This solves our many problems and also make everything easy and nice.



# Builder Facet

Sometime using one builder doesn't satisfy our requirements. Then we can use multiple builder to build an Object.

Exmaples in: **builder_facets.py**


# Builder Inheritance

When using multiple Builder we shouldn't forget about our **SOLID** principles. To comply with the open-close (Open for Extention and Closed for modification) we can use the Inheritance of OOP design.

Examples are in: **builder_inheritance.py**