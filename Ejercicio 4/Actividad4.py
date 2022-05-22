import pdb
#pdb.set_trace()
from itertools import filterfalse
""""En esta parte se definen los """
lista =[[2, 12, 8, 9, 10], [4, 24, 120, 300, 10], [5, 20, 1, 50, 2]]
listap =  [3, 4, 8, 5, 5, 22, 13, 169, 181, 203, 11]
def mayor():

    numayor = 0

    for i in range(3):
        """ Esta función recoge dentro de cada objeto de la lista el mayor número"""
        numayor = 0
        for j in range(5):
            num=lista[i][j]
            if (num>numayor):
                lista[i][j]= numayor
                numayor=num
        if(numayor !=0):
            print(numayor)

print(mayor())

def condicion(numero):
    for n in range(2, numero):
        """Esta función recoge la condicion para saber si un número es primo"""
        if numero % n == 0:
            return False
    return numero

def primos():
    """Esta función imprime los números primos que se encuentran
    dentro de nuestra lista"""
filtrada = list(filter(condicion, listap))
print(f"Números primos {filtrada}")
