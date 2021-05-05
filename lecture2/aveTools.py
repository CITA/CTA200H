

try:
    xrange   # If we are running Python 2, xrange will be ok
except NameError:
    xrange =  range   # If not, (xrange does not exist in Python 3), redefine xrange


def onedl(rows):
    return [None] * rows

def twodl(rows, cols):
    a=[]
    for row in xrange(rows): a += [[None]*cols]
    return a


def threedl(rows, cols, depth):
    a=[]
    for row in xrange(rows): 
        a += [[None]*cols]
        for col in xrange(cols): 
            a[row][col] = [None]*depth
    return a


def fourdl(rows, cols, depths1, depths2):
    
    a = [[[[None for x in xrange(depths2)] for x in xrange(depths1)] for x in xrange(cols)] for x in xrange(rows)]

    return a


def onedDict(names1):

    output = {}
    for a in names1:
        output[a] = {}
    return output

def twodDict(names1, names2):

    output = {}
    for a in names1:
        output[a] = {}
        
        for b in names2:
            output[a][b] = {}
            

    return output


def threedDict(names1, names2, names3):

    output = {}
    for a in names1:
        output[a] = {}
        
        for b in names2:
            output[a][b] = {}
            
            for c in names3:
                output[a][b][c] = {}

    return output

def fourdDict(names1, names2, names3, names4):

    output = {}
    for a in names1:
        output[a] = {}
        
        for b in names2:
            output[a][b] = {}
            
            for c in names3:
                output[a][b][c] = {}

                for d in names4:
                    output[a][b][c][d] = {}

    return output

def fivedDict(names1, names2, names3, names4, names5):

    output = {}
    for a in names1:
        output[a] = {}
        
        for b in names2:
            output[a][b] = {}
            
            for c in names3:
                output[a][b][c] = {}

                for d in names4:
                    output[a][b][c][d] = {}

                    for e in names5:
                        output[a][b][c][d][e] = {}

    return output
