import requests
try:
    arquivo = open('admin.txt')
except:
    print("arquivo não encontrado")

linhas = arquivo.readlines()
def busca(linhas):

    url = 'http://ahnegao.com.br/'
    for linha in linhas:
        resposta = requests.get(url+linha)

        if resposta.status_code != 404:
            print (url+linha, resposta.status_code)

