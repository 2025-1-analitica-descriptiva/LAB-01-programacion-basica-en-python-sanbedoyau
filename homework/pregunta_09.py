from homework.utils import loadFile, linePreprocessing, mapper09, shuffleAndSort

def pregunta_09():
    '''
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5
    R/=
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}
    '''
    seq = loadFile('files/input/data.csv')
    seq = linePreprocessing(seq)
    seq = mapper09(seq)
    seq = shuffleAndSort(seq)
    return dict(seq)