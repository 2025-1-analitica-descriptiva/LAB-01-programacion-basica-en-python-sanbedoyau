from homework.utils import loadFile, linePreprocessing, mapper11, shuffleAndSort

def pregunta_11():
    '''
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente
    R/= {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}
    '''
    seq = loadFile('files/input/data.csv')
    seq = linePreprocessing(seq)
    seq = mapper11(seq)
    seq = shuffleAndSort(seq)
    return dict(seq)