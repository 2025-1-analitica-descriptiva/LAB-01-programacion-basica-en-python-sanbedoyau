from homework.utils import loadFile, linePreprocessing, mapper02, shuffleAndSort, reducer
def pregunta_02():
    '''
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente
    R/= [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    '''
    seq = loadFile('files/input/data.csv')
    seq = linePreprocessing(seq)
    seq = mapper02(seq)
    seq = shuffleAndSort(seq)
    return reducer(seq)