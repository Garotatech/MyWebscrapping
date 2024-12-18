Este projeto é dedicado ao Web Scraping, abrangendo a extração de dados tanto de sites quanto de APIs. Para facilitar o aprendizado e a organização, o trabalho foi dividido em três scripts, cada um responsável por realizar a raspagem de dados de fontes distintas.

# Tecnologias Utilizadas

- **Python**: Linguagem utilizada no projeto.
- **Selenium**: Biblioteca utilizada para interagir com o navegador e elementos da página web
- **BeautifulSoup**: Biblioteca utilizada para extrair conteúdos HTML da Web.

## Requisitos:
- Python 3.7 ou superior
- Bibliotecas:
  - `Selenium`
  - `BeautifulSoup`  

# Projeto:
## 1 Funcionalidade - Desafio 1: Web Scraping do Reddit.
Utilizando as bibliotecas Requests e BeautifulSoup, este script faz o web scraping do título, up votes e link das três primeiras postagens do subreddit r/programming no Reddit. Os dados coletados utilizando a biblioteca BeautifulSoup, Re dentre outras e suas informações são armazenados em Json.


## 2° Funcionalidade - Desafio 2: Extração de dados de ofertas de uma API.
Neste exercício, foi feito web scraping a partir de uma resposta JSON de simulando uma API de um e-commerce. O objetivo principal é extrair uma lista de ofertas com os seguintes atributos:

- offer_link: link da oferta
- image_link: link da imagem do produto
- price: preço da oferta


## 3° Funcionalidade - Desafio 3: Captura de Informações de produtos da Magazine Luiza
Este script captura informações de produtos diretamente do site Magazine Luiza e então estrutura as informações em formato JSON. Os atributos coletados incluem:

- title: título do produto
- stock_availability: disponibilidade em estoque
- price: preço do produto



