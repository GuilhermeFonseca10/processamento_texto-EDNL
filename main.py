import string
import time
import re
import nltk

nltk.download('stopwords')
#retiro as stopwords 
stopwords = nltk.corpus.stopwords.words("portuguese")

#ler o arquivo e conta a frequencia das palavras e busca.
#recebe como parametro nome_arquivo que é o arquivo a ser lido, e a lista de palavra
def contar_palavras(nome_arquivo, palavras_para_buscar):

#abre o arquivo e armazena na variavel texto
    with open(nome_arquivo, encoding="utf-8") as arquivo:
        texto = arquivo.read()
# remove os caracteres de pontuação do texto usando expressão regular
    texto = re.sub(f"[{string.punctuation}]", "", texto)
# divide o texto em uma lista de palavra
    palavras = texto.split()
#cria uma lista com todas as palavras com letras minusculas
    palavras_minusculas = [palavra.lower() for palavra in palavras]
#armazena a contagem de cada palavra
    contagem_palavras = {}
#percore cada palavra e adiciona a contagem
    for palavra in palavras_minusculas:
    #se a palavra estiver nas stopwords, não adiciona no dicionário
        if palavra not in stopwords:
            contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
    palavra_mais_comum = max(contagem_palavras, key=contagem_palavras.get)
    
    contagem_palavras_buscadas = {}
    posicoes_palavras = {}

    for palavra in palavras_para_buscar:
        palavra_para_comparar = palavra.lower()
        #pega o valor da contagem da palavra buscada, ou 0 se não estiver no dicionario
        contagem_palavras_buscadas[palavra] = contagem_palavras.get(palavra_para_comparar, 0)
        
    #gera uma lista das posições dos indices em palavras minusculas que é a ocorrência da palavra
    #armazena as contagens e posições das palavras buscadas nos dicionarios contagem_palavras_buscadas e posições_palavras.
        posicoes_palavras[palavra] = [i for i, w in enumerate(palavras_minusculas) if w == palavra_para_comparar]
   #retorna os 4 valores
    return contagem_palavras_buscadas, palavra_mais_comum, contagem_palavras[palavra_mais_comum], posicoes_palavras

nome_arquivo = input("Digite o nome do arquivo: ")
palavras_para_buscar = input("Digite as palavras para buscar, separadas por vírgulas: ").split(",")

inicio_tempo = time.time()
contagem_palavras_buscadas, palavra_mais_comum, contagem, posicoes_palavras = contar_palavras(nome_arquivo, palavras_para_buscar)

for palavra in palavras_para_buscar:
    print(f"#{palavra}")
    print(f"Frequência: {contagem_palavras_buscadas[palavra]}")
    print(f"Posições: {', '.join(str(p) for p in posicoes_palavras[palavra])}")
    print()

print(f"\nA palavra mais frequente no arquivo é '{palavra_mais_comum}' com {contagem} ocorrências.")
print
