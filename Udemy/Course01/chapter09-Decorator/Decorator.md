# Decorator

The motivation behind the decorator design patter is to enhance the class without modifying it. Adding behvior without altering the class itself.

Sometimes you have a class and you want to augment with additional functionality. You do not want rewrite or alter existing code (Open close principle). You want to keep new functionality seperate (Single Responsibility Principle). But you need to somehow be able to interact with existing structures. 

Now you have two options for that:
- Inherit from required object (if possible)
- Build a decorator which simply references the decorated object(s) nd you add additional behavior on top of that



### Functional Decorator
In python we have already known something called functional decorator.

This is a function.

```
def some_op():
  print('Starting op')
  time.sleep(1)
  print('We are done')
  return 123
```

we want to decorate it with additional feature. We do this by using pythons decorator feature.
```
def time_it(func):
  def wrapper():
    start = time.time()
    result = func()
    end = time.time()
    print(f'{func.__name__} took {int((end-start)*1000)}ms')
  return wrapper
```


here, **func** the reference to the function we want to decorate.


### Classical Decorator

The classical implementation od decorator is, you build a class the kinds of augments the functionality you want to add in on the existing class.
Example in **classical_decorator.py**

### Dynamic Decorator

The down side of the classical decorator is that you might not have a method avilable in the decorator that is available in the object. Like the **resize**  in the classical decorator example.

For that, we can use some dynamic programming in python. We can use pythons built in feature that will let us use the feature in object from the decorator.

Well it has a downside too, of being slow a little. But that is something you have to give up if you want additional feature to wrap with your object.

Examples in **functional_decorators.py**

