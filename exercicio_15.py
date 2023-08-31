# 15) Leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a apenas em dias.

anos = input ("Insira sua idade em anos: ")
meses = input ("Insira os meses completos: ")
dias = input ("Insira os dias ")

total_dias = ((int(anos)*365)+(int(meses)*30)+int(dias))

print ("Você viveu: ", total_dias, "dias.")
print ("\nALUNOS: \n  Gustavo dos Santos Silva    G72FDE9 \n  Guilherme Aparecido Banhe   N060BG7 \n") #identificação dos alunos
print ("PROFESSOR: \n   Medina \n IPE") #identificação do professor e da matéria