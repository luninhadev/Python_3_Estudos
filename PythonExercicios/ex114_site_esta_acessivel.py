'''
DESAFIO 114

Crie um código em python que teste se o site Pudim está acessivel pelo computador usado.
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site Pudim não está acessível no momento.\033[m')
else:
    print('\033[32mConsegui acessar o site Pudim com sucesso!\033[m')

'''
print(site.read()) -> Pega o conteúdo HTML do site
'''
