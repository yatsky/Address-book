import os

class addressBook:
    def __init__(self, bookName, bookPath):
        self.name = bookName
        self.path = bookPath
        self.bookDir = bookPath + os.sep + self.name

        if not os.path.exists(self.bookDir):
            print 'Creating the book.'
            book = open(self.bookDir, 'w')
            book.write('This is a addressbook. :)\n')
            book.close()

    def printInfo(self):
        print "Book name: {0}, book path: {1}".format(self.name, self.bookDir)

bookPath = raw_input('Please specify the location: ')
bookName = raw_input('Please specify the name: ')
book1 = addressBook(bookName, bookPath)
