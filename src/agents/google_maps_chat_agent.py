# src/agents/google_maps_agent.py
from typing import Dict, Any
from .base import BaseAgent
from src.services.search_service import SearchService
from src.utils.prompts import GOOGLE_MAPS__REVIEWS_PROMPT

class GoogleMapsChatAgent(BaseAgent):
    def __init__(self):
        super().__init__()
        self.search_service = SearchService()
    
    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        restaurant_name = state["restaurant_name"]
        location = state["location"]

        # Construir el prompt
        prompt = GOOGLE_MAPS__REVIEWS_PROMPT.format(
            restaurant_name=restaurant_name,
            location=location)
        
        # Realizar búsqueda con OpenAI
        search_results = self.search_service.search(
            query=f"{restaurant_name} {location} Google Maps",
            prompt=prompt
        )
        
        # Actualizar el estado
        state["google_maps_data"] = search_results
        state["status"] = "google_maps_completed"
        
        return state