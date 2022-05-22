class Error(Exception):
    pass
class mesesexactos(Error):
    pass

def suma(x,y):
    return x+y

def CalculaMedia(a,b,x,y,z):
    return (a+b+x+y+z)/5

def Mayus(a,b):
    return a==b

def meses(a, b):
        try:
            if(a==b):
                raise mesesexactos
        except mesesexactos:
            return False
        else:
            return True

def longitud(a,b):
    return a+b;
