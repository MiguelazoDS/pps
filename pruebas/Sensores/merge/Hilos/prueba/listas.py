import random

def modif(lista):
    print()
    lista[0]=10000

def main():
    lista = [random.randint(0,10) for i in range(10)]
    print(lista)
    modif(lista)
    print(lista)
    
if __name__ == '__main__':
    main()
