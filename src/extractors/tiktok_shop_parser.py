thonimport requests
from bs4 import BeautifulSoup

class TikTokShopParser:
    def __init__(self, url):
        self.url = url
        self.product_data = []

    def extract_product_data(self):
        response = requests.get(self.url)
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve the webpage, status code: {response.status_code}")

        soup = BeautifulSoup(response.text, 'html.parser')

        products = soup.find_all('div', class_='product-container')
        for product in products:
            title = product.find('h3', class_='product-title').get_text(strip=True)
            price = product.find('span', class_='price').get_text(strip=True)
            rating = product.find('span', class_='rating').get_text(strip=True)
            sold = product.find('span', class_='sold').get_text(strip=True)
            product_link = product.find('a', href=True)['href']
            image_url = product.find('img', src=True)['src']

            product_info = {
                'title': title,
                'price': price,
                'rating': rating,
                'sold': sold,
                'product_link': product_link,
                'image_url': image_url
            }
            self.product_data.append(product_info)

        return self.product_data