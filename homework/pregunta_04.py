from homework.utils import loadFile, linePreprocessing, mapper04, shuffleAndSort, reducer
def pregunta_04():
    '''
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación
    R/=
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    '''
    seq = loadFile('files/input/data.csv')
    seq = linePreprocessing(seq)
    seq = mapper04(seq)
    seq = shuffleAndSort(seq)
    return reducer(seq)