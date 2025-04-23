# src/services/search_service.py
import openai
from typing import Dict, Any, List
import os
import json

class SearchService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=self.api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4.1")
    
    def search(self, query: str, prompt: str) -> Dict:
        """
        Realiza una búsqueda web a través de OpenAI
        """
        # Usando el modelo con capacidad de búsqueda web
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Eres un asistente de búsqueda que ayuda a encontrar información específica sobre restaurantes."},
                {"role": "user", "content": prompt}
            ],
            tools=[{
                "type": "function",
                "function": {
                    "name": "search_web",
                    "description": "Busca información en la web",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "La consulta de búsqueda"
                            }
                        },
                        "required": ["query"]
                    }
                }
            }],
            tool_choice={"type": "function", "function": {"name": "search_web"}}
        )
        
        # Obtener la consulta de búsqueda generada
        tool_calls = response.choices[0].message.tool_calls
        search_query = json.loads(tool_calls[0].function.arguments).get("query")
        
        # Realizar la búsqueda real
        search_results = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Extrae información específica sobre el restaurante y devuélvela en formato JSON estructurado."},
                {"role": "user", "content": f"Busca: {search_query}\n\nAnaliza los resultados y extrae información sobre: {prompt}"}
            ],
            response_format={"type": "json_object"}
        )
        
        return json.loads(search_results.choices[0].message.content)