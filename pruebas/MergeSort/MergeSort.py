import sys, time, random

#La función merge comienza con una comparación entre dos listas de
#tamaño 1. Las listas sucesivas que recibe luego están ordenadas
def merge(izq, der):
    lst_ord = []
    ind_izq = ind_der = 0
    while ind_izq < len(izq) and ind_der < len(der):
        if izq[ind_izq] <= der[ind_der]:
            lst_ord.append(izq[ind_izq])
            ind_izq += 1
        else:
            lst_ord.append(der[ind_der])
            ind_der += 1
    if ind_izq == len(izq):
        lst_ord.extend(der[ind_der:])
    else:
        lst_ord.extend(izq[ind_izq:])
    return lst_ord

#Divide una lista hasta que obtiene solo un elemento y envía ese valor a "merge"
def mergesort(lst):
    if len(lst) > 1:
        ind = len(lst)//2
        mitad_izq = lst[:ind]
        mitad_der = lst[ind:]
        return merge(mergesort(mitad_izq),mergesort(mitad_der))
    else:
        return lst

def main():
    #Tamaño por defecto de la lista
    N=1000000
    #Comprueba que se haya pasado un parámetro
    if len(sys.argv) > 1:
        #Si es un número genera la lista entre 0 y 1000 de N elementos
        if sys.argv[1].isdigit():
            N = int(sys.argv[1])
            lista = [random.randint(0,1000) for i in range(N)]
            print ("Se generó una lista aleatoria de %d elementos" % (N))
        #Si no es un número sale del programa
        else:
            print ("El valor ingresado no es un número")
            exit(1)
    start = time.time()
    mergesort(lista)
    final = time.time() - start
    print ("El algoritmo demoró %f segundos" % (final))

if __name__ == '__main__':
    main()
