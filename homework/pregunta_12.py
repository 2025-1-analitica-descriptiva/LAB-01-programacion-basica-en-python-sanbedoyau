from homework.utils import loadFile, linePreprocessing, mapper12, shuffleAndSort

def pregunta_12():
    '''
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo
    R/= {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    '''
    seq = loadFile('files/input/data.csv')
    seq = linePreprocessing(seq)
    seq = mapper12(seq)
    seq = shuffleAndSort(seq)
    return dict(seq)