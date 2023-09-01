# funcoes.py

def mensagem():
    return "Olá, Mundo!"
#

# funcoes.py

def cumprimentar(nome):
    return f"Olá, {nome}!"

#PRIMEIRA FUNÇÃO ^^^

# principal.py

from funcoes import cumprimentar

def main():
         nome = input("Digite o seu nome: ")
         mensagem = cumprimentar(nome)
         print(mensagem)

if __name__ == "__main__":
      main()

#SEGUNDA FUNÇÃO ^^^         