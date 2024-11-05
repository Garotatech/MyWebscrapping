# Observação Importante: No momento, não encontramos informações sobre a quantidade de produtos disponíveis em estoque no site da Magazine Luiza.

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import logging
import re
from datetime import datetime

global driver,now
driver = webdriver.Chrome()
now = datetime.now()


def get_products():
    
    try:    
        driver = webdriver.Chrome() 
        url = "https://www.magazineluiza.com.br/busca/notebooks/?from=submit"
        driver.get(url)
        time.sleep(3)
    
        html_content = driver.page_source
        htlm_soup = BeautifulSoup(html_content, 'html.parser')
        product_list = htlm_soup.find_all("li", {"class": "sc-knefzF ktOmEl"})
        
        return product_list
    
    except NoSuchElementException:
        print("Erro: O elemento especificado não foi encontrado no DOM.")
        
        
def get_informations(product_list):  
    
    products = []
    for product in product_list:
        try:
            title = product.find("h2", {"data-testid": "product-title"})
            title = title.get_text(strip=True) if title else "Título não encontrado"
            price = product.find("p", {"data-testid": "price-value"})
            price = price.get_text(strip=True) if price else "Preço não encontrado"
            price= re.search(r"[\d.]+,\d+", price).group()
            
            # Embora o exercicio peça para estruturas as informações em um Json, preferi inserir as informações em uma lista de dicionários para uma melhor visualização. 
            products.append({
                "Title": title,
                "Price": price
            })
        except TypeError as e:
            logging.error(f"Erro de tipo: {e}")
        except ValueError as e:
            logging.error(f"Erro de valor ao extrair preço: {e}")
            
    print("A busca utilizando Python levou o total de: " + str((datetime.now() - now).total_seconds()) + " segundos.")
    return products

driver.quit()




def main():
   products_list =  get_products()
   all_produtos_sale = get_informations(products_list)
    
if __name__ == "__main__":
    main()