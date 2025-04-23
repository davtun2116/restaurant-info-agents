# src/services/openai_service.py
import openai
from typing import Dict, Any, List
import os
import json

class OpenAIService:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = openai.OpenAI(api_key=self.api_key)
        self.model = os.getenv("OPENAI_MODEL", "gpt-4o")
    
    def generate_structured_data(self, prompt: str) -> Dict:
        """
        Genera datos estructurados a partir de un prompt
        """
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Eres un asistente experto en extraer y estructurar información sobre restaurantes."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"}
        )
        
        return json.loads(response.choices[0].message.content)