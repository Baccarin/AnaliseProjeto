import random
import time

vetor = list(range(0,10)) #gera vetor
random.shuffle(vetor)

bubble = vetor.copy() #Bubble Sort
print("Antes da operação")
print(bubble)

def bubble_sort(bubble):
    fim = len(bubble)

    while fim > 0:
        i = 0
        #percorrendo o vetor de zero até fim
        while i < fim-1:
            if bubble[i] > bubble[i+1]:
                temporario = bubble[i]
                bubble[i] = bubble[i+1]
                bubble[i+1] = temporario
            i += 1
        fim -= 1

antes = time.time()
bubble_sort(bubble)
depois = time.time()

total = (depois - antes)*1000

print("Depois da operação")
print(bubble)

print("Bubble sort: %0.2f ms" % total)