'''
10) Entrar via teclado com o valor de cinco produtos. 
Após as entradas, digitar um valor referente ao pagamento da somatória destes valores. 
Calcular e exibir o troco que deverá ser devolvido.
'''

produto_1 = input ("Entre com o valor do produto: ")    # O usuário insere o valor do primeiro produto
produto_2 = input ("Entre com o valor do produto: ")    # O usuário insere o valor do segundo produto
produto_3 = input ("Entre com o valor do produto: ")    # O usuário insere o valor do terceiro produto
produto_4 = input ("Entre com o valor do produto: ")    # O usuário insere o valor do quarto produto
produto_5 = input ("Entre com o valor do produto: ")    # O usuário insere o valor do quinto produto

valor_recebido = input ("Digite o valor que será usado no pagamento: ")

troco = int(valor_recebido) - (int(produto_1)+int(produto_2)+int(produto_3)+int(produto_4)+int(produto_5))

print ("Troco: ", troco)
print ("\nALUNOS: \n  Gustavo dos Santos Silva    G72FDE9 \n  Guilherme Aparecido Banhe   N060BG7 \n") #identificação dos alunos
print ("PROFESSOR: \n   Medina \n IPE") #identificação do professor e da matéria