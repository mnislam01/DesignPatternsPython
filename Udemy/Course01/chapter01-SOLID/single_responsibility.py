class Journal(object):

    def __init__(self):
        self.entries = []
        self.counter = 0

    def add_entry(self, text):
        self.counter += 1
        self.entries.append(f'{self.counter}: {text}')

    def del_entry(self, indx):
        del self.entries[indx]
        self.counter -+ 1

    def __str__(self):
        return '\n'.join(self.entries)



class JournalManager(object):

    @staticmethod
    def save(journal, filename):
        the_file = open(filename, 'w')
        the_file.write(str(journal))
        the_file.close()

    def load(journal, filename):
        pass

    def load_from_web(journal, uri):
        pass


j = Journal()
j.add_entry("I ate a banana")
j.add_entry("I am writing code")

file = "journal.txt"

JournalManager.save(j, file)

with open(file) as fp:
    print(fp.read())


print(j)

