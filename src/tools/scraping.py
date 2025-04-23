import requests
from bs4 import BeautifulSoup
from ..utils.logging import get_logger

logger = get_logger(__name__)

def fetch_page(url: str) -> str:
    """
    Descarga el contenido HTML de la URL dada.
    """
    logger.debug(f"Fetching URL: {url}")
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def parse_restaurant_page(html: str) -> dict:
    """
    Parsea el HTML de una página de restaurante y extrae datos clave.
    """
    soup = BeautifulSoup(html, 'html.parser')
    data = {
        'menu': None,
        'average_price': None,
        'services': [],
        'images': []
    }
    # Extraer menú
    menu = soup.select_one('.menu')
    if menu:
        data['menu'] = menu.get_text(strip=True)
    # Extraer precio medio
    price = soup.select_one('.average-price')
    if price:
        data['average_price'] = price.get_text(strip=True)
    # Servicios
    services = [s.get_text(strip=True) for s in soup.select('.service')]
    data['services'] = services
    # Imágenes destacadas
    imgs = [img['src'] for img in soup.select('.gallery img')]
    data['images'] = imgs
    logger.debug(f"Parsed restaurant page data: {data}")
    return data

class ScraperToolkit:
    def get_tools(self):
        return [
            {'name': 'fetch_page', 'func': fetch_page, 'description': 'Descarga HTML de una URL'},
            {'name': 'parse_page', 'func': parse_restaurant_page, 'description': 'Parses HTML y extrae datos'}
        ]


def get_scraper_tools() -> ScraperToolkit:
    """
    Devuelve un toolkit de scraping para agentes.
    """
    return ScraperToolkit()