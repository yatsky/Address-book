import os

class addressBook:
    def __init__(self, bookName, bookPath):
        self.name = bookName
        self.path = bookPath
        self.bookDir = bookPath + os.sep + self.name

        if not os.path.exists(self.bookDir):
            print 'Creating the book.'
            book = open(self.bookDir, 'w')
            book.write('This is an addressbook. :)\n')
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

    def add(self, userInput):
        '''Add new pair of address and name into the file'''
        book = open(self.bookDir, 'a')
        book.write(userInput + '\n')
        book.close()


action1 = 'Add info'
action2 = 'Browse the book'
action3 = 'Search the book'
bookPath = raw_input('Please type the path of the book.\n')
bookName = raw_input('Please type the name of the book.\n')
action = raw_input('''What do you want to do?
Please select:
{0}
{1}
{2}\n'''.format(action1, action2, action3))

if action == action1:
    book = addressBook(bookName, bookPath)
    book.printInfo()
    userInput = raw_input('Please type the name and address.')
    book.add(userInput)

elif action == action2: #Browse
    book = addressBook(bookName, bookPath)
    book.printInfo()
    userInput = raw_input('Please tell me how many lines you want to see.')
    book.browse(userInput)

elif action == action3: #Search the book
    book = addressBook(bookName, bookPath)
    book.printInfo()
    userInput = raw_input('Please tell me what you want to know.')
    book.search(userInput)
 
else:
    print 'I cannot understand this command now, maybe type later.' 