# Seu trabalho é extrair uma lista com as ofertas resultantes da pesquisa. O objetivo é extrair os atributos principais das ofertas. Exemplo de pesquisa: https://www.climario.com.br/geladeira?_q=geladeira&map=ft List of:
# offer_link > link da oferta
# image_link > link da imagem do produto
# price > preço da oferta

import requests
import pandas
import json
import re
from collections import defaultdict


def get_json():

    path_json = 'data/api_response.json'
    with open(path_json, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    return dados

def get_produtos(dados):
    # A função get_profutos percorre os valores e busca as informações de preço, link da imagem e link do produto, então retorna um dicionário com os valores obtidos.
    
    ofertas = []
    produtos = defaultdict(dict)
    pattern = re.compile(r"sp-(\d+)")

    for chave, valor in dados.items():
        match = pattern.search(chave)
        if match:
            produto_id = match.group(1)
            produtos[produto_id][chave] = valor
            
    # A estrutura de loop percorre a chave que contem as informações dos links dos produtos
    for chave, valor in produtos.items():
        try:
            for item in produtos[chave]:
                try:
                    # Validando se realmente existe a chave que contem as informações dos links 
                    if item in ['Product:sp-' + chave, '$Product:sp-'+chave+'.priceRange.sellingPrice']:
                        if 'description' in produtos[chave][item]:                    
                            conteudo = re.search(r'<img src="([^"]+)"', produtos[chave][item]['description'])
                            if conteudo and 'https' in conteudo.group(1):
                                image_link = conteudo.group(1)
                                offer_link = image_link.rsplit('/', 1)[0]
                        elif item == '$Product:sp-'+chave+'.priceRange.sellingPrice' and 'highPrice' in produtos[chave][item]:            
                            price = produtos[chave][item]['highPrice']
                            if price and conteudo:
                                ofertas.append({"Image_link": image_link,
                                                    "Offer_link": offer_link,
                                                    "Price": price})         
                except KeyError as e:
                    print(f"Erro de chave não encontrada: {e}")
        except Exception as e:
            print(f"Erro geral no processamento do produto {chave}: {e}")
                    
              
    return ofertas
                        
                                
def main():   
    
    dados = get_json()
    ofertas = get_produtos(dados)
    if ofertas:
        print("A lista com os resultados foi gerada com sucesso!")
    
if __name__ == '__main__':
    main()