from homework.utils import loadFile, linePreprocessing, mapper03, shuffleAndSort, reducer
def pregunta_03():
    '''
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente
    R/= [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    '''
    seq = loadFile('files/input/data.csv')
    seq = linePreprocessing(seq)
    seq = mapper03(seq)
    seq = shuffleAndSort(seq)
    return reducer(seq)