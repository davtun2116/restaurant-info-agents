from langchain.tools import Tool
from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults

# Herramientas de búsqueda
class CustomSerpAPIWrapper(SerpAPIWrapper):
    def __init__(self):
        super().__init__()
    
    def run(self, query: str) -> str:
        """Run query through SerpAPI and parse result."""
        search_params = {
            "engine": "google_maps",
            "q": query,
            "google_domain": "google.es",  # Puedes ajustar según el país
            "hl": "es",  # Idioma en español
            "type": "search",
            "num": "10",  # Número de resultados
        }
        return self._process_response(search_params)


def get_google_maps_search_tool() -> Tool:
    """
    Devuelve una tool de Google Maps Search
    """
    serpapi_maps = CustomSerpAPIWrapper()
    return Tool(
        name="GoogleMapsSearch",
        description="Busca restaurantes y obtiene información detallada de Google Maps como ubicación, horarios, valoraciones, precios, etc.",
        func=serpapi_maps.run,
    )

def get_web_search_tool() -> Tool:
    """
    Devuelve una tool de tavily search
    """
    tavily_search = TavilySearchResults(k=5)
    return Tool(
        name="WebSearch",
        description="Búsqueda web general para encontrar información adicional sobre el restaurante, reseñas, página web, etc.",
        func=tavily_search.invoke,
    )

# Herramienta para búsqueda específica de reseñas
def search_reviews(query: str) -> str:
    """Busca reseñas específicas del restaurante que mencionen palabras clave relacionadas con gluten."""
    serpapi_maps = CustomSerpAPIWrapper()
    search_params = {
        "engine": "google_maps_reviews",
        "q": query + " gluten celíaco",
        "google_domain": "google.es",
        "hl": "es",
        "sort_by": "relevance",  # Ordenar por relevancia
        "num": "15",  # Más reseñas para encontrar menciones específicas
    }
    return serpapi_maps._process_response(search_params)

def get_review_search_tool() -> Tool:
    """
    Devuelve una tool de review search
    """
    return Tool(
        name="ReviewsSearch",
        description="Busca reseñas específicas que mencionen palabras clave como gluten, celiaco, etc.",
        func=search_reviews,
    )
