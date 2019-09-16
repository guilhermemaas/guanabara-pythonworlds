"""
Faça um programa que leia um número inteiro e retorne na tela seu sucessor e antecessor.
"""

numero = int(input('Digite um número para validar seu sucessor e antecessor: '))

print('O número digitado é: {}.\nSeu sucessor é: {}.\nSeu antecessor é {}.'.format(numero, numero-1, numero+1))
