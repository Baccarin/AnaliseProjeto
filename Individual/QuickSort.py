import random
import time

vetor = list(range(0,10)) #gera vetor
random.shuffle(vetor)

quickSort = vetor.copy() #Quick Sort
print("Antes da operação")
print(quickSort)

def quick_sort(quickSort, p, r):
  if p < r: #Condicao de Parada (ou condicao de existencia)
      q = particionar(quickSort, p, r)
      quick_sort(quickSort, p, q-1) #Pivotar a Esquerda (Ordenar os elementos menores do que o Pivô)
      quick_sort(quickSort, q+1, r) #Pivotar a Direita (Ordenar os elementos maiores do que o Pivô)

def particionar(quickSort, p, r):
  x = quickSort[p] #Escolhendo o Pivo (É o primeiro elemento da esquerda)
  i = p #Destino final do Pivô
  j =  p + 1 #Contador para percorrer o restante do vetor

  while j<= r: #Percorrer o vetor
      if quickSort[j] < x: #detectou-se um elemento menor que o pivô, incrementa o i
          i += 1
          trocar(quickSort, i, j)
      j += 1 #passa para o proximo elemento

  trocar(quickSort, p, i)

  return i

def trocar(v, n, m):
  temp = quickSort[n]
  quickSort[n] = quickSort[m]
  quickSort[m] = temp

antes = time.time()
quick_sort(quickSort, 0, len(quickSort)-1)
depois = time.time()

print("Depois da operação")
print(quickSort)


total = (depois - antes)


print("Quick Sort %10f" %total)
