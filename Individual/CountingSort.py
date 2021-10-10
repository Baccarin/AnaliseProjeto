import random
import time


x = 10
vetor = list(range(0,x)) #gera vetor
random.shuffle(vetor)
#print(vetor)
##Cada vX desse corresponde a um algoritmo de ordenação,
# dessa forma é posssivel testar a performace com o mesmo vetor em todos eles!

coutingSortVector = vetor.copy() #Counting Sort
print("Antes da operação")
print(coutingSortVector)


def countingSort(array):
  tamanho = len(array)
  saida = [0] * tamanho

  # Inicializar o array contador
  contador = [0] * x
  # Guarde a quantidade de cada elemento no array contador
  for i in range(0, tamanho):
      contador[array[i]] += 1
  # Guarda a conta acumulativa
  for i in range(1, 10):
      contador[i] += contador[i - 1] 
  # Encontre o index de cada elemento do array original no array contador
  # Coloque os elementos no array de saida
  i = tamanho - 1
  while i >= 0:
      saida[contador[array[i]] - 1] = array[i]
      contador[array[i]] -= 1
      i -= 1
  # Copia os elementos ordenados para o array original
  for i in range(0, tamanho):
      array[i] = saida[i]

antes = time.time()
countingSort(coutingSortVector)
depois = time.time()
total = (depois - antes)

print("Depois da operação")
print(coutingSortVector)

print("Counting Sort: %2f" % total)