# aula 9

# atividade 1

# 1

n = 0
while n<= 1000:
    print(n)
    n = n + 1
    
# 2

nomes = []

for n in range(1,11):
    nome = input('Digite seu nome')
    nomes.append(nome)
print(nomes)

# atividade 2

# 1

usuario_correto = "aluno"
senha_correta = "1234"

tentativas = 0
acesso_concedido = False

while tentativas < 3:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    
    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!\n")
        acesso_concedido = True
        break
    else:
        tentativas += 1
        print(f"Usuário ou senha incorretos. Tentativas restantes: {3 - tentativas}\n")

if not acesso_concedido:
    print("Conta bloqueada. Tente novamente mais tarde.")
else:
    
    notas = []
    num_notas = int(input("Quantas notas deseja inserir? "))

    for i in range(num_notas):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)

    media = sum(notas) / len(notas)
    print(f"\nNotas inseridas: {notas}")
    print(f"Média final: {media:.2f}")

    if media >= 7:
        print("Status: Aprovado")
    elif media >= 5:
        print("Status: Recuperação")
    else:
        print("Status: Reprovado")
