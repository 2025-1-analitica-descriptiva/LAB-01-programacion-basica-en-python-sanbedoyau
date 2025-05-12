from homework.utils import loadFile, linePreprocessing, mapper10

def pregunta_10():
    '''
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5
    R/=
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    '''
    seq = loadFile('files/input/data.csv')
    seq = linePreprocessing(seq)
    return mapper10(seq)