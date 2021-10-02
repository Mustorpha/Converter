from Bank import Bank
from Engine import Engine

def converter (value):
    try:
        value = int(value)
    except ValueError:
        raise ValueError ('The converter works with integers only')
    placeValue = []
    grandValue = []
    result = []
    flag = 0
    machine = Engine(value)
    machine.splitOrder()
    mac = machine._Engine__new
    machine.evaluator(mac)
    mas = machine._Engine__answer
    for values in mas:
        for value in values:
            if 'hundred' in value:
                ind = values.index(value)
                if values[ind+1]:
                    values[ind] += ' and'
    for num in range(len(mas)):
        grandvalue = ((10**3)**num)
        placeValue.append(grandvalue)
    grandvalue = machine.read(placeValue)
    for grands in grandvalue:
        grandValue.append(grands)
    grandValue.reverse()
    for num in range(len(grandValue)-1):
        mas[num].append(grandValue[num])
    placeValue.clear()
    for values in mas:
        try:
            result = machine.join(values)
            placeValue.append(result)
        except TypeError :
            raise TypeError ('Limit exceeded, extend the bank dictionary')
            
    result = machine.join(placeValue)
    print(result)
        
