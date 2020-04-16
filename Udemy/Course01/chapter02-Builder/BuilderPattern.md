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

