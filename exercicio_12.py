'''
12) Crie  um programa  que permita  informar  o  valor  total  da  compra  e  exiba  os  valores  que  
Dona Maria irá pagar no total em cada uma das formas de pagamento e os valores de cada parcela, 
caso a mesma opte por dividir.
'''

valor = input ("insira o valor do produto: ")
a_vista = int(valor)*0.9
parcelado = int(valor)/3
vezes_10 = (float(valor))+(float(valor)*0.05)
print ("Métodos de pagamento: \n")
print ("a) A vista com 10 por cento de desconto: ", a_vista, ".")
print ("b) Parcelado em 1+2 vezes de %.2f sem desconto:" %parcelado, (int(parcelado)*3))
print ("c) Dividido em 10 vezes com juros de 5 por cento sobre o valor total: ", vezes_10)
print ("\nALUNOS: \n  Gustavo dos Santos Silva    G72FDE9 \n  Guilherme Aparecido Banhe   N060BG7 \n") #identificação dos alunos
print ("PROFESSOR: \n   Medina \n IPE") #identificação do professor e da matéria