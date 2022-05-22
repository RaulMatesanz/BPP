import pandas as pd

csv = pd.read_csv("C:/Users/Raul/Desktop/Master/Buenas_Prácticas_de_Programacion_en_Python/Tema1/Práctica/finanza.csv"
,engine="python", thousands='.', decimal=',', sep='\t')
print()
gastoE = csv["Enero"].tolist()
gastoF = csv["Febrero"].tolist()
gastoM = csv["Marzo"].tolist()
gastoA = csv["Abril"].tolist()
gastoMa = csv["Mayo"].tolist()
gastoJ= csv["Junio"].tolist()
gastoJu = csv["Julio"].tolist()
gastoAg = csv["Agosto"].tolist()
gastoS = csv["Septiembre"].tolist()
gastoO = csv["Octubre"].tolist()
gastoN = csv["Noviembre"].tolist()
gastoD = csv["Diciembre"].tolist()
gastoMeses = gastoE + gastoF + gastoM + gastoA + gastoMa + gastoJ +gastoJu + gastoAg + gastoS + gastoO + gastoN + gastoD
media = csv.mean()
minimo = csv.min()
maximo=csv.max()
mayor=0
maximonum = 0
num = 0
mes = 0
menor = 0
menornum = 0
numero = 0
madiat = 0.0
mediatotal = 0.0
gastot = 0
gastototal = 0
ingreso = 0
ingresoTotal = 0
columnas = 0
datoerror = 0
datocorrecto = 0
class Error(Exception):
    pass
class mesesexactos(Error):
    pass
class haycontenido(Error):
    pass

for i in range(len(maximo)):
    try:
        num=int(maximo[i])
    except ValueError:
        print("")
    else:
        maximonum=num
        if maximonum>mayor:
            mayor=maximonum
            mes = i+1

print("El máximo ahorrado es: ", mayor, "y se encuentra en el mes número:", mes)

for i in range(len(minimo)):
    try:
        numero=int(minimo[i])
    except ValueError:
        print("Eso no es un numero")
    else:
        menornum=numero
        if menornum<menor:
            menor=menornum
            mes = i+1
print("El mayor gasto es: ", menor, "y se encuentra en el mes número:", mes)

for i in range (len(media)):
    try:
        mediat=float(media[i])
    except ValueError:
        print("Eso no es un numero")
    else:
        mediatotal+= mediat

print("La media total del año es", mediatotal/12)

for i in range (len(gastoMeses)):
    try:
        gastot=int(gastoMeses[i])
    except ValueError:
        print("Eso no es un numero")
    else:
        if gastot<0:
            gastototal+= gastot


print("El gasto total del año es: ", gastototal)
for i in range (len(gastoMeses)):
    try:
        ingreso=int(gastoMeses[i])
    except ValueError:
        print("Eso no es un numero")
    else:
        if ingreso>0:
            ingresoTotal+= ingreso
print("Los ingresos totales del año han sido: ", ingresoTotal)

# APARTADO 2

    #Probar que existe el fichero
try:
    print(csv)

except IOError as err:
    print("No encuentro el fichero o no puedo leerlo. Error: ", err)
else:
    print("He leido el fichero sin problema")

#Probar que el fichero tiene 12 columnas
    try:
        if(len(maximo)==11):
            raise mesesexactos
    except mesesexactos:
        print("El fichero no tiene 12 columnas")
    else:
        print("El fichero tiene 12 columnas")

# Probar que hay contenido para cada mes
#Lo podría haber calculado todo junto con la lista que cree, pero al poner
#en específico cada mes, supuse que había que crear un try para cada uno por separado
#Enero

    try:
        for i in range (len(gastoE)):
            if(len(gastoE[i]) != 0):
                raise haycontenido
    except haycontenido:
        print("La columna Enero contiene un dato vacio")
    else:
        print("La columna Enero no contiene un dato vacio")
#Febrero
    try:
        for i in range (len(gastoF)):
            if(gastoF[i] == 0):
                print(gastoF)
                raise haycontenido
    except haycontenido1:
        print("La columna Febrero contiene un dato vacio")
    else:
        print("La columna Febrero no contiene un dato vacio")
#Marzo
        try:
            for i in range (len(gastoM)):
                if gastoM[i] == 0:
                    raise haycontenido
        except haycontenido:
            print("La columna Marzo contiene un dato vacio")
        else:
            print("La columna Marzo no contiene un dato vacio")
#Abril
    try:
        for i in range (len(gastoA)):
            if gastoA[i] == 0:
                raise haycontenido
    except haycontenido:
        print("La columna Abril contiene un dato vacio")
    else:
        print("La columna Abril no contiene un dato vacio")
#Mayo
        try:
                for i in range (len(gastoMa)):
                    if gastoMa[i] == 0:
                        raise haycontenido
        except haycontenido:
            print("La columna Mayo contiene un dato vacio")
        else:
            print("La columna Mayo no contiene un dato vacio")
#Junio
            try:
                for i in range (len(gastoJ)):
                    if gastoJ[i]== 0:
                        raise haycontenido
            except haycontenido:
                print("La columna Junio contiene un dato vacio")
            else:
                print("La columna Junio no contiene un dato vacio")
#Julio
            try:
                for i in range (len(gastoJu)):
                    if(len(gastoJu[i]) == 0):
                        raise haycontenido
            except haycontenido:
                print("La columna Julio contiene un dato vacio")
            else:
                print("La columna Julio no contiene un dato vacio")
#Agosto
            try:
                for i in range (len(gastoAg)):
                    if gastoAg[i] == 0:
                        raise haycontenido
            except haycontenido:
                print("La columna Agosto contiene un dato vacio")
            else:
                print("La columna Agosto no contiene un dato vacio")
#Septiembre
            try:
                for i in range (len(gastoS)):
                    if(len(gastoS[i]) == 0):
                        raise haycontenido
            except haycontenido:
                print("La columna Septiembre contiene un dato vacio")
            else:
                print("La columna Septiembre no contiene un dato vacio")
#Octubre
            try:
                for i in range (len(gastoO)):
                    if(len(gastoO[i]) == 0):
                        raise haycontenido
            except haycontenido:
                print("La columna Octubre contiene un dato vacio")
            else:
                print("La columna Octubre no contiene un dato vacio")
#Noviembre
            try:
                for i in range (len(gastoN)):
                    if(len(gastoN[i]) == 0):
                        raise haycontenido
            except haycontenido:
                print("La columna Noviembre contiene un dato vacio")
            else:
                print("La columna Noviembre no contiene un dato vacio")
#Diciembre
            try:
                for i in range (len(gastoD)):
                    if(gastoD[i] == 0):
                        raise haycontenido
            except haycontenido:
                print("La columna Diciembre contiene un dato vacio")
            else:
                print("La columna Diciembre no contiene un dato vacio")

# Comprobar que todos los datos son correctos
for i in range (len(gastoMeses)):
    try:
        int(gastoMeses[i])
    except ValueError:
        datoerror += 1
    else:
        datocorrecto += 1

print("Se han introducido correctamente ", datocorrecto, "datos y no se han introducido bien ", datoerror)
