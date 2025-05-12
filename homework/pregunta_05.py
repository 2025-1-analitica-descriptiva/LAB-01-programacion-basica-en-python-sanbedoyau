from homework.utils import loadFile, linePreprocessing, mapper05, shuffleAndSort

def pregunta_05():
    '''
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1
    R/= [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]
    '''
    seq = loadFile('files/input/data.csv')
    seq = linePreprocessing(seq)
    seq = mapper05(seq)
    return shuffleAndSort(seq)