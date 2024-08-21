"""
Faça um jogo para o usuario adivinhar qual a palavra secreta.
- Voce vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Qual o usuário digitar apenas uma letra.
- Qual o usuário digitar uma letra, voce vai conferir se a letra digitada esta na palavra secreta.
    - Se a letra digitada estriver na palavra secreta; exiba a letra;
    - Se a letra digitada nao estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""


palavra_secreta = 'futebol' # Define a palavra secreta que o usuário deve adivinhar. Neste caso, a palavra é "futebol".

letraCerta = '' # ria uma variável letraCerta, que começa como uma string vazia. Esta variável vai armazenar as letras que o usuário acertou até agora.

tentativas = 0 # Inicializa a variável tentativas com o valor 0. Esta variável vai contar quantas tentativas o usuário fez para adivinhar a palavra secreta.

print("Voce iniciou o jogo da palavra secreta.")

while True:

    letra = input("Digite uma letra: ").lower()

    if len(letra) > 1:
        print("Digite apenas uma letra.")
        continue
    elif letra in palavra_secreta:
        letraCerta += letra
    # Verifica se a letra digitada está na palavra secreta. Se estiver, adiciona essa letra à string letraCerta, que armazena todas as letras corretas que o usuário adivinhou até agora.

    palavraFormada = ''

    for letraSecreta in palavra_secreta:
        if letraSecreta in letraCerta:
            palavraFormada += letraSecreta
        else:
            palavraFormada += "*"
    # Este bloco de código percorre cada letra da palavra_secreta.
    # Se a letra da palavra secreta estiver na lista de letras adivinhadas (letraCerta), ela é adicionada a palavraFormada.
    # Se a letra não estiver em letraCerta, um asterisco (*) é adicionado a palavraFormada, representando uma letra ainda não adivinhada.
    
    tentativas += 1

    print(f"palavra formada: {palavraFormada}")

    if palavraFormada == palavra_secreta:
        print(f"A palavra secreta era ( {palavra_secreta.upper()} )")
        print(f"Parabens voce acertou a palavra com {tentativas} tentativas!")
        break
    


    

    