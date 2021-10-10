import random
import time

vetor = list(range(0,10)) #gera vetor
random.shuffle(vetor)

insertionSort = vetor.copy() #Insertion Sort
print("Antes da operação")
print(insertionSort)

def insertion_sort(insertionSort):
    i = 1
    while i < len(insertionSort):
        temporario = insertionSort[i]
        trocou = False
        j = i - 1
        while j >= 0 and insertionSort[j] > temporario:
            insertionSort[j+1] = insertionSort[j]
            trocou = True
            j -= 1

        if trocou:
            insertionSort[j+1] = temporario
        i += 1

antes = time.time()
insertion_sort(insertionSort)
depois = time.time()

total = (depois - antes)*1000
print("Depois da operação")
print(insertionSort)

print("Insertion Sort: %0.2f ms" % total)