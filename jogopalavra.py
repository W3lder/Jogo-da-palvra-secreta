"""
Faça um jogo para o usuario adivinhar qual a palavra secreta.
- Voce vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Qual o usuário digitar apenas uma letra.
- Qual o usuário digitar uma letra, voce vai conferir se a letra digitada esta na palavra secreta.
    - Se a letra digitada estriver na palavra secreta; exiba a letra;
    - Se a letra digitada nao estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""


palavraSecreta = 'fortnite'

letraCerta = ''

tentativas = 0

print("Voce comecou o jogo da palavra secreta!")

while True:

    Letra = input("Digite uma letra: ").lower()

    if len(Letra) > 1:
        print("Digite uma letra.")
        continue
    elif Letra in palavraSecreta:
        letraCerta += Letra
    
    palavraFormada = ''

    for letraSecreta in palavraSecreta:
        if letraSecreta in letraCerta:
            palavraFormada += letraSecreta
        else:
            palavraFormada += "*"

    tentativas += 1

    print(f"palavra formada: {palavraFormada}")

    if palavraFormada == palavraSecreta:
        print("PARABENS VOCE ACERTOU A PALAVRA.")
        print(f"Tentativas: {tentativas}")
        break