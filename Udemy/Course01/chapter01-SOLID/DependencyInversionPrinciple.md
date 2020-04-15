The basic idea of Dependency Inversion Principle is that, an A base class should never depend on an inherited class, instead both of them should depend on abstraction(abstract class/method)[another way of saying, interface].


Simply, change in a low level module should not break a high level module.

To fix that we can use some abstraction or interface or implement things in low level module that highlevel module can use.


For example, lets say we have a low level class **Todo**. It has concerns about storing the data and other stuff.

```
class Todo(object):
    def __init__(self):
        self.todo_list = []

    def add_todo(self, text):
        self.todo_list.append(text)
```

Now let's make a high level module that uses that class.


```
class ListTodos(object):
    def __init__(self, todo)
        self.all_todos = todo.todo_list

    def list(self):
        return self.all_todos.sort()
```


Here, if the **todo_list** storage type changes in **Todo** class. Then it will affect the high level class **SortTodos**.

We can fix that by introducing abstract class **BaseTodo**.

```
class BaseTodo(object):
    @abstractmethod
    def sort_in_ascending_order(self): pass
```

and we can inherit from that in **Todo** class.

```
class Todo(BaseTodo):
    def __init__(self):
        self.todo_list = []

    def add_todo(self, text):
        self.todo_list.append(text)

    def sort_in_ascending_order(self):
        return self.all_todos.sort()
```

And also change the **ListTodos** class like following:

```
class ListTodos(object):
    def __init__(self, todo)
        self.todo = todo
    
    def list(self):
        self.todo.sort_in_ascending_order()
```


In that way we have eleminated the dependancy of High level class **ListTodos** from low level class **Todo**. And if we need to change the low level things like the data type of todos_list we can do that simply in **BaseTodo** without chaning **Todo** and **ListTodos**.

That is the idea of Dependency Inversion principle.