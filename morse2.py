if __name__== "__main__":
    with open('morse.in') as entrada:
        with open('morse.out', 'W') as saida:
            morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
            "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

#realiza a leitura de todas as linhas do arquivo de entrada
linhas = entrada.readlines()

#Laço que percorre a linha
for linha in linhas:
    #retira o fim de linhas e espaços
    temp = linha.rstrip('\n').split(" ")
    #cria uma variável vazia
    palavra = ""

    #novo laço que percorre a linha tratada
    for t in temp:
        #inicia um contador
        cont = 0

        #laço percorre a variável morse e comparar com os elementos
        for p in morse:
            if(t==p):
                '''se for encontrada a letra
                a palavra recebeela mesma mais a letra convertida'''
                palavra += chr(65 + cont)
                break
            cont += 1
            
        saida.write(palavra+'\n')
        if (linha == '..-. ..--'):
            break