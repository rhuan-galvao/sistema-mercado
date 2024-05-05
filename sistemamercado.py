import json
import os

print('\033[32m'+'-------------------------------------------------\n               Sistema de Mercado!\n-------------------------------------------------'+'\033[0;0m\n\033[32m'+'[0] Ver lista de produtos\n[1] Adicionar produto\n[2] Remover produto'+'\033[0;0m\n')

while True:
    filename = 'E:/PYTHON/produtos.json'
    list_obj = []

    if not os.path.isfile(filename):
        print('Você não tem um arquivo, criando um.')
        with open(filename, 'w') as file:
            json.dump(list_obj, file)

    with open(filename) as fp:
        list_obj = json.load(fp)
    
    try:
        inpt = int(input('O que você deseja fazer?: '))
          
        if inpt == 0:
            for products in list_obj:
                for idx, product in enumerate(list_obj, start=1):
                    print(f"{idx}. Tipo: {product['Tipo']}\n   Produto: {product['Produto']}")
        elif inpt == 1:
            inpt_type = input('Digite o tipo do produto: ')
            inpt_product = input('Digite o nome do produto: ')
            list_obj.append({
                'Tipo': inpt_type,
                'Produto': inpt_product
            })
            print('Produto adicionado')
        elif inpt == 2:
            inpt_type = input('Digite o tipo do produto: ')
            inpt_product = input('Digite o nome do produto: ')
            to_remove = None
            for product in list_obj:
                if product['Tipo'] == inpt_type and product['Produto'] == inpt_product:
                    to_remove = product
            if to_remove:
                list_obj.remove(to_remove)
                print('Produto removido!\n')
            else:
                print('Produto não encontrado!')
    except ValueError:
        print('Digite um número correto!\n')

    with open(filename, 'w') as json_file:
        json.dump(list_obj, json_file,
                indent=4,
                separators=(',', ': ')) 
