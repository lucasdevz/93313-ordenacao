"""
Dada uma lista de palavras, escreva um programa
que solicite ao usuário uma lista de frutas e mostre:
- a lista original
- a lista ordenada
- a lista inversa

Caso o usuário digite sair, pare de solicitar dados.

REFATORANDO CÓDIGO:
Crie uma função para:
- Ordenação
- Ordenação na ordem inversa
"""

import os
os.system("cls || clear")
lista_frutas = ["Manga", "Uva", "Amora", "Caju"]

print("Lista original")
print(lista_frutas)

#Modificando a lista original
lista_organizada = sorted(lista_frutas, reverse= True)

print("\nLista ordenada")
print(lista_organizada)

lista_frutas.sort(reverse= True)
print("\nLista inversa")
print(lista_frutas)
