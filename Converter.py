from Processor.Bank import Bank
from Processor.Engine import Engine

def converter (value):
    try:
        value = int(value)
    except ValueError:
        raise ValueError ('The converter works with integers only')
    placeValue = []
    grandValue = []
    result = []
    flag = 0
    processor = Engine(value)
    processor.splitOrder()
    mac = processor._Engine__new
    processor.evaluator(mac)
    mas = processor._Engine__answer
    for values in mas:
        for value in values:
            if 'hundred' in value:
                ind = values.index(value)
                try:
                    if values[ind+1]:
                        values[ind] += ' and'
                except IndexError:
                    continue
    for num in range(len(mas)):
        grandvalue = ((10**3)**num)
        placeValue.append(grandvalue)
    grandvalue = processor.read(placeValue)
    for grands in grandvalue:
        grandValue.append(grands)
    grandValue.reverse()
    for num in range(len(grandValue)-1):
        if len(mas[num]) == 0:
            continue
        mas[num].append(grandValue[num])
    placeValue.clear()
    for values in mas:
        try:
            result = processor.join(values)
            placeValue.append(result)
        except TypeError :
            raise TypeError ('Limit exceeded, extend the bank dictionary')
            
    result = processor.join(placeValue).strip()
    result = result.removesuffix(',')
    print(result)
