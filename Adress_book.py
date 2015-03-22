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

    #look for the infomation pertaining to user input
    def search(self, userInput):
        with open(self.bookDir) as file:
            for index, line in enumerate(file, 1):
                if userInput in line:
                    print 'Found in ',line
            else:
                print '{} is not in this book!'.format(userInput)

    def browse(self, userInput):
        '''User types a number indicating how many lines
        she wants to see.'''
        with open(self.bookDir) as file:
            for i in range(1, userInput + 1):
                print file.readline()

bookPath = raw_input('Please specify the location: ')
bookName = raw_input('Please specify the name: ')
book1 = addressBook(bookName, bookPath)
userInput = int(raw_input('Type what you are looking for.'))
book1.browse(userInput)
