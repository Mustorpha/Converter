'''
The Engine class for the converter
it holds contains all the methods necessary
for the machine to successfully convert dynamically
The design is such that an instance of the engine
class can be created explicitly for any purpose
'''

from Bank import Bank

class Engine (Bank):
    """
    Operates on the data the bank holds
    """

    def __init__ (self, value): #initializes the classe 
        self.value = value
        self.__number = []
        self.__placeValue = []
        self.__answer = []
        self.__new = []
            
    def splitOrder (self):
        '''
        split the instance value into
        a list of three values per element
        starting from the right side
        '''
        
        self.__new.clear()
        value = str(self.value) #stringed the value for easy slicing
        flag = len(value)
        
        # slice the string into three character per value
        for strings in value:
            if flag <= 2:
                determinant = 0
            else:
                determinant = flag - 3
            result = value[determinant:flag]
            self.__new.append(result)
            flag -= 3
            if flag < 0:
                break
        self.__new.reverse()
        try:
            for digits in self.__new:
                self.__new.remove('')
        except ValueError:
            return
            
    def placeValue (self, item):
        '''
        find the place value of items in a listed format
        '''
        
        self.__placeValue.clear()
        for values in range(0, len(item)):
            values = 10**values     #10^index gives the mirrored place value list for the elements in the list in order of arragement
            self.__placeValue.append(values)
        self.__placeValue.reverse()   #reverse the place value list for correct indexing

    def read (self, item):
        '''
        reads through the bank class with the item as the key
        yield the corresponding values and placevalues
        '''

        for items in item:     #  reads through the item, return once when it is one
            if items in Engine.bank.values():
                for key in Engine.bank.keys():
                    if Engine.bank[key] == items:
                        yield key
            else:
                yield None
    def join (self, iterates):
        '''
        join iterates with a space
        '''

        result = list(iterates) #list the iterates for conveniency 
        result = ' '.join(result)
        return result
    
    def evaluator (self, items):
        '''
        works on a list and evaluates their value
        into another list
        '''
        
        for value in items:
            Engine.placeValue(self, value)
            flag = 0
            temp = []
            temp.clear()
            for num in value:
                self.__number.clear()
                self.__number.append((int(num))*self.__placeValue[flag])  #multiply values with their place value and then read their values from the bank
                flag += 1
                iterates = Engine.read(self, self.__number)
                for iterate in iterates:
                    temp.append(iterate)
            self.__answer.append(temp)
        
        #remove empty values in each sublist to avoid translation by the program
        self.__answer = [[word for word in parts if word != ''] for parts in self.__answer]