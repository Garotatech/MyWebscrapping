Projeto de Web Scraping
Este projeto realiza web scraping em diferentes fontes de dados para coletar informações relevantes de postagens do subreddit r/programming, ofertas de um e-commerce e informações de produtos do Magazine Luiza.

Atividades Realizadas
Questão 1: Web Scraping do Reddit
Utilizando as bibliotecas Requests e BeautifulSoup, este script faz o web scraping do título, up votes e do link das três primeiras postagens do subreddit r/programming no Reddit. Os dados coletados são armazenados em Json.


# Lógica para coletar dados do Reddit
Questão 2: Extração de Ofertas de um E-commerce
Neste exercício, foi feito web scraping a partir de uma resposta JSON de uma API de um e-commerce. O objetivo é extrair uma lista de ofertas com os seguintes atributos:

offer_link: link da oferta
image_link: link da imagem do produto
price: preço da oferta
title: título da oferta


# Lógica para processar o arquivo api_response.json
Questão 3: Captura de Informações do Magazine Luiza
Este script captura informações de produtos diretamente do site Magazine Luiza e estrutura os dados em formato JSON. Os atributos coletados incluem:

title: título do produto
stock_availability: disponibilidade em estoque
price: preço do produto

# Lógica para coletar dados do Magazine Luiza
