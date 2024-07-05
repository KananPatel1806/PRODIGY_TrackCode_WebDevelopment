import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_product_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    
    for item in soup.find_all('div', class_='s-item__info'):
        name = item.find('h3', class_='s-item__title')
        price = item.find('span', class_='s-item__price')
        rating = item.find('div', class_='b-starrating')
        
        if name and price:
            product_name = name.text
            product_price = price.text
            product_rating = rating.text if rating else 'No rating'
            
            products.append({
                'Name': product_name,
                'Price': product_price,
                'Rating': product_rating
            })
    
    return products

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

# Example usage
url = 'https://www.ebay.com/sch/i.html?_nkw=laptop'
product_data = get_product_info(url)
save_to_csv(product_data, 'products.csv')
print(f"Data saved to products.csv")
