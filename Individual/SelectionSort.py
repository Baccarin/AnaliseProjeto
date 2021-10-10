import random
import time

vetor = list(range(0,10)) #gera vetor
random.shuffle(vetor)
print("Antes da operação")
print(vetor)

selectionSort = vetor.copy() #Selection Sort

def selection_sort(selectionSort):
    i = 0
    while i < len(selectionSort) - 1:
        menor = i
        j = i + 1
        while j < len(selectionSort):
            if selectionSort[j] < selectionSort[menor]:
                menor = j
            j += 1

        if menor != i:
            temporario = selectionSort[i]
            selectionSort[i] = selectionSort[menor]
            selectionSort[menor] = temporario
        i += 1

antes = time.time()
selection_sort(selectionSort)
depois = time.time()

total = (depois - antes)*1000
print("Depois da operação")
print(selectionSort)

print("Selection Sort: %0.2f ms" % total)
