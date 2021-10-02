'''
The Engine class for the converter
it holds contains all the methods necessary
for the machine to successfully convert dynamically
'''

import Bank
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
        for strings in value:
            if flag <= 2:
                det = 0
            else:
                det = flag - 3
            result = value[det:flag]
            self.__new.append(result)
            flag -= 3
            if flag < 0:
                break
        self.__new.reverse()
        try:
            for dig in self.__new:
                self.__new.remove('')
        except ValueError:
            return
            
    def placeValue (self, item):
        '''
        find the place value of items
        in a listed format
        in simulation to the basic
        hundred-tens-unit
        '''
        
        self.__placeValue.clear()
        for values in range(0, len(item)):
            values = 10**values     #10^index gives the place value list
            self.__placeValue.append(values)
        self.__placeValue.reverse()   #revers the place value list for correct indexing

    def read (self, item):
        '''
        reads through the bank class
        with the item as the key
        yield the corresponding values
        '''

        for items in item:     #  reads through the item, return once when it is one
            if items in Engine.bank.values():
                for key in Engine.bank.keys():
                    if Engine.bank[key] == items:
                        result = key
                        yield result
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
        works on a list and
        evaluates their value
        into another list
        '''
        
        for value in items:
            Engine.placeValue(self, value)
            flag = 0
            temp = []
            temp.clear()
            for num in value:
                self.__number.clear()
                self.__number.append((int(num))*self.__placeValue[flag])  #multiply values with their place value and then read them into the bank
                flag += 1
                iterates = Engine.read(self, self.__number)
                for iterate in iterates:
                    temp.append(iterate)
            self.__answer.append(temp)
        for lin in self.__answer:
            try:
                lin.remove('')    #get rid of zero-empty pair in the list
            except ValueError:    #handles when the loop goes larger than the avaliable event to stop indexError from raising
                continue
