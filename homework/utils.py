#
# Archivo auxiliar para la definición de funciones, los
# archivos de las preguntas tienen el rol de orquestador
#

def loadFile(input: str):
    with open(input) as file:
        sequence = file.readlines()
    return sequence

def linePreprocessing(sequence: list):
    seq: list = [line.replace('\n', '') for line in sequence]
    seq: list = [line.split('\t') for line in seq]
    return seq

##############################################

def mapper02(sequence: list):
    return [(line[0], 1) for line in sequence]

def mapper03(sequence: list):
    return [(line[0], int(line[1])) for line in sequence]

def mapper04(sequence: list):
    return [(line[2].split('-')[1], 1) for line in sequence]

def mapper05(sequence: list):
    min: dict = {}
    max: dict = {}
    for line in sequence:
        if (line[0] not in min.keys()) or (line[0] not in max.keys()):
            max[line[0]] = int(line[1])
            min[line[0]] = int(line[1])
            continue
        if int(line[1]) > max[line[0]]:
            max[line[0]] = int(line[1])
        if int(line[1]) < min[line[0]]:
            min[line[0]] = int(line[1])
    return zip(min.keys(), max.values(), min.values())

def mapper06(sequence: list):
    min: dict = {}
    max: dict = {}
    seq: list = [line[4].split(',') for line in sequence]
    seq: list = [line.split(':') for lines in seq for line in lines]
    for key, value in seq:
        if (key not in min.keys()) or (key not in max.keys()):
            min[key] = int(value)
            max[key] = int(value)
            continue
        if int(value) > max[key]:
            max[key] = int(value)
        if int(value) < min[key]:
            min[key] = int(value)
    return zip (min.keys(), min.values(), max.values())

def mapper07(sequence: list):
    numbers: dict = {}
    seq: list = [(int(line[1]), line[0]) for line in sequence]
    for key, value in seq:
        if key not in numbers.keys():
            numbers[key] = []
        numbers[key].append(value)
    return list(numbers.items())

def mapper08(sequence: list):
    numbers: dict = {}
    seq: list = [(int(line[1]), line[0]) for line in sequence]
    for key, value in seq:
        if key not in numbers.keys():
            numbers[key] = []
        if value not in numbers[key]:
            numbers[key].append(value)
    for key in numbers.keys():
        numbers[key] = sorted(numbers[key])
    return list(numbers.items())

def mapper09(sequence: list):
    count: dict = {}
    seq: list = [line[4].split(',') for line in sequence]
    seq: list = [line.split(':')[0] for lines in seq for line in lines]
    for key in seq:
        if key not in count.keys():
            count[key] = 0
        count[key] += 1
    return count.items()

def mapper10(sequence: list):
    return [(line[0], len(line[3].split(',')), len(line[4].split(','))) for line in sequence]

def mapper11(sequence: list):
    sum: dict = {}
    seq: list = [(line[3], int(line[1])) for line in sequence]
    seq: list = [(letter, value) for keys, value in seq for letter in keys.split(',')]
    for key, value in seq:
        if key not in sum.keys():
            sum[key] = 0
        sum[key] += value
    return list(sum.items())

def mapper12(sequence: list):
    suma: dict = {}
    aux_dict: dict = {}
    seq: list = [(line[0], line[4]) for line in sequence]
    for key, value in seq:
        if key not in aux_dict.keys():
            aux_dict[key] = []
        aux_dict[key]+= value.split(',')
    for key in aux_dict.keys():
        dictionary = [int(item.split(':')[1]) for item in aux_dict[key]]
        suma[key] = sum(dictionary)
    return list(suma.items())

##############################################

def shuffleAndSort(sequence: list):
    return sorted(sequence, key = lambda x: x[0])

def reducer(sequence: list):
    red = {}
    for key, value in sequence:
        if key not in red.keys():
            red[key] = 0
        red[key] += value
    return list(red.items())