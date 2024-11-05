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
        url = "https://www.reddit.com/r/programming/"
        driver.get(url)
        time.sleep(3)
    
        html_content = driver.page_source
        htlm_soup = BeautifulSoup(html_content, 'html.parser')
        product_list = htlm_soup.find_all("article", {"class": "w-full m-0"})
        upvotes = htlm_soup.find('faceplate-number')
        
        return product_list, upvotes
    
    except NoSuchElementException:
        print("Erro: O elemento especificado não foi encontrado no DOM.")
        
        
def get_informations(product_list,upvotes):  
    
    products = []
    for product in product_list:
        try:

            text = product.find("shreddit-post").text.replace('\n', ' ')
            text = ' '.join(text.split())
            match = re.search(r'^(.*?)(https?://|u/|ADMIN|MOD|há|•|$)', text)
            if match:
                title = match.group(1).strip()  # Captura o título
            else:
                title = text.strip()
            url = re.search(r'https?://[^\s]+', text)
            url = url.group(0) if url else None
                
            #upvotes = upvotes.text
            #upvotes = re.search(r'pretty number=(\d+)', upvotes)
            #pretty_number = upvotes.group(1)
                
            products.append({
                "Title": title,
                "link": url,
                "uoVotes": None
            })    
        except TypeError as e:
            logging.error(f"Erro de tipo: {e}")
        except ValueError as e:
            logging.error(f"Erro de valor ao extrair preço: {e}")
            

    return products





driver.quit()


def main():
   products_list, upvotes =  get_products()
   all_produtos_sale = get_informations(products_list,upvotes)
    
if __name__ == "__main__":
    main()