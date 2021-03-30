import os
from sort import (
    insertionSort,
    mergeSort
)
from test import test


def makeTest(filePath, sortingAlgorithms, deltas):
    assert(len(sortingAlgorithms) == len(deltas))
    # Runs the tests and saves them in filePath (assumes is a file path string)
    testFile = open(filePath, "w")
    testFile.write("")
    testFile.close()
    
    for i in range(len(deltas)):
        test(filePath, sortingAlgorithms[i], deltas[i])

def main():
    path = os.getcwd() + "/test.txt"

    print("Este es un script de pruebas para algoritmos de ordenamiento.")
    print("Las pruebas pueden tomar varias horas.")
    print("Los resultados se guardarán en \"{0}\". Si el archivo ya existe,".format(path)
        + " su contenido será borrado y reemplazado.")
    
    while (inpt := input("¿Desea iniciar con las pruebas? (s/n): ")) != "n":
        if inpt == "s":
            makeTest(path, [insertionSort, mergeSort], [100, 5000])
            break
        else:
            continue
    

if __name__ == "__main__":
    main()
