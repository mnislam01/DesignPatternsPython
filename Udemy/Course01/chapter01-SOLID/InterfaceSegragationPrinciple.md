Simply interface substitution principle says that, if we use an interface, we should not make one interface with every fatures. Instead, what we should do is, making seperate and smallest interface possible for fatures. 


For example lets say, we are building a Printer client (class). Now, we made the following **Machine** interface with options **printing**, **scanning** and **faxing**, because we are smart.

```
class Machine:
    def print(self, document):
        raise NotImplementedError()

    def fax(self, document):
        raise NotImplementedError()

    def scan(self, document):
        raise NotImplementedError()

```

Now, let's use it.

```
class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def fax(self, document):
        pass

    def scan(self, document):
        pass

```

It's okay if the Printer is Multifunction Printer. But let's say I don't want a Multifunctioning Printer. I want limited functioning printer. Then I could cripple some of the featues, let's say, I want only a Printer that can Print. Nothing more. to do that we can do.


```
    def print(self, document):
        pass

    def fax(self, document):
        pass  # do-nothing

    def scan(self, document):
        """Not supported!"""
        raise NotImplementedError('Printer cannot scan!')

```


But it doesn't makes sense. I wanted a printer that can only Print, it does that, that is fine. But there are **fax** and **scan** options I can see but can't use. That is disturbing. Simply it doesn't makes sense.

So, to make it better for the client of the interface what we could do is, making Smaller interfaces and join multiple interfaces if needed. Like:


```
class Printer:
    @abstractmethod
    def print(self, document): pass


class Scanner:
    @abstractmethod
    def scan(self, document): pass


class MyPrinter(Printer):
    def print(self, document):
        print(document)


class MySmartPrinter(Printer, Scanner)
    def print(self, document):
        print(document)

    def scan(self, document):
        pass # do scanning
```

If we need a MultifunctioningDevice interface we could have that too by:

```
class MultiFunctionDevice(Printer, Scanner):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass
```

And build MultifunctioningPrinter

```
class MultiFunctionMachine(MultiFunctionDevice):
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def print(self, document):
        self.printer.print(document)

    def scan(self, document):
        self.scanner.scan(document)
```

That way we eleminate the burden of keeping things that we don't require and making the design more usefull and flexible.
