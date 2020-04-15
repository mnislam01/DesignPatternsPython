Objects are for a purpuse and for a single purpuse only.
A class should have a single reason to change and should 
be related to it's primary responsibiliy.

A class should not be over loaded with features.


Let's say we have a class called **Jurnal**. It's responsibility is to let user add an entry to it, remove and entry from it and to store the entries.

```
class Journal(object):
    def __init__(self):
        pass
    
    def add_entry(self, text):
        pass

    def del_entry(self, text):
        pass
```

Don't give a class such responsibilites that it never asked for. 

So out Journal class has 

**add_entry, del_entry** methods. It does what it's was asked for. Till now the pattern is okay. 

Let's say we want to give it some more responsibilities like, saving those entries in a file.

so, we added more methods like:

**save, load, load_from_web**

Journal class has now things that it didn't ask for. It breaks the pattern. It's it anti-pattern.

To fix that, what we should do is, create a new class for those responsibilites.

```
class JournalManager(object):

    @staticmethod
    def save(journal, finename):
        pass

    @staticmethod
    def load(journal, filename):
        pass

    @staticmethod
    def load_from_web(journal, uri):
        pass
```

So the idea is we don't want to overload our Class with responsibilites.
