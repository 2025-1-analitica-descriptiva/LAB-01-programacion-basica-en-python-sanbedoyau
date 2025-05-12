from homework.utils import loadFile, linePreprocessing

def pregunta_01():
    '''
    Retorne la suma de la segunda columna
    R/= 214
    '''
    seq = loadFile('files/input/data.csv')
    seq = linePreprocessing(seq)
    return sum([int(line[1]) for line in seq])