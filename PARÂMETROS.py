# parâmetros  == variáveis vazias que precisam ser preenchidas
# nós substituimos paramestros por argumentos

def mostrar_dados(nome, idade):
    print('nome', nome,'idade', idade)
    

mostrar_dados('Julia', 21)
mostrar_dados('Marcos', 16)
mostrar_dados('Maria', 14)



def test_lista(lista):
    s = sum(lista)
    print('Total', s)
    

lista = [1,2,3,6,5,9,8]
test_lista(lista)


def teste_dicionarios(d):
    for n in d.items():
        print(n)
        

dicionario1  = {'a':250, 'b':270}
dicionario2  = {'c':500, 'd':300}
dicionario3  = {'e':700, 'f':1000}

teste_dicionarios(dicionario1)
teste_dicionarios(dicionario2)
teste_dicionarios(dicionario3)

