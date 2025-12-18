from scraper.fetcher import fetch_html
from scraper.parser import parse_products
from scraper.saver import save_to_csv

def main():
    url = "https://example.com/products"
    
    html = fetch_html(url)
    products = parse_products(html)
    save_to_csv(products)

    print(f"{len(products)} produits enregistrés")

if __name__ == "__main__":
    main()
