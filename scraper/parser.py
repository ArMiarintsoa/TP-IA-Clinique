from bs4 import BeautifulSoup

def parse_products(html):
    soup = BeautifulSoup(html, "lxml")

    products = []
    items = soup.find_all("div", class_="product")

    for item in items:
        title = item.find("h2").get_text(strip=True)
        price = item.find("span", class_="price").get_text(strip=True)

        products.append({
            "title": title,
            "price": price
        })

    return products
