def coletar_e_analisar_dados():
    alturas = []
    generos = []

    # Coleta de dados de 15 pessoas
    for i in range(1, 16):
        print(f"\nColetando dados da pessoa {i}:")

        while True:
            try:
                altura = float(input("Digite a altura (em metros, ex: 1.75): "))
                if altura <= 0:
                    print("A altura deve ser um valor positivo. Tente novamente.")
                else:
                    alturas.append(altura)
                    break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número para a altura.")

        while True:
            genero = input("Digite o gênero (M para Masculino, F para Feminino): ").upper()
            if genero in ['M', 'F']:
                generos.append(genero)
                break
            else:
                print("Entrada inválida. Por favor, digite 'M' ou 'F'.")

    # Inicialização de variáveis para análise
    maior_altura = max(alturas)
    menor_altura = min(alturas)

    soma_altura_masculino = 0
    cont_masculino = 0
    cont_feminino = 0

    # Análise dos dados
    for i in range(len(alturas)):
        if generos[i] == 'M':
            soma_altura_masculino += alturas[i]
            cont_masculino += 1
        elif generos[i] == 'F':
            cont_feminino += 1

    # Cálculo da média de altura masculina
    media_altura_masculino = soma_altura_masculino / cont_masculino if cont_masculino > 0 else 0

    # Apresentação dos resultados
    print("\n--- Resultados da Análise ---")
    print(f"A maior altura do grupo é: {maior_altura:.2f} metros")
    print(f"A menor altura do grupo é: {menor_altura:.2f} metros")

    if cont_masculino > 0:
        print(f"A média de altura das pessoas do gênero Masculino é: {media_altura_masculino:.2f} metros")
    else:
        print("Não foram inseridos dados para pessoas do gênero Masculino.")

    print(f"O número de pessoas do gênero Feminino é: {cont_feminino}")


# Executa a função
coletar_e_analisar_dados()