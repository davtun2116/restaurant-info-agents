# src/agents/base.py
from abc import ABC, abstractmethod
from typing import Dict, Any
from src.services.openai_service import OpenAIService

class BaseAgent(ABC):
    def __init__(self):
        self.openai_service = OpenAIService()
    
    @abstractmethod
    def run(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Ejecuta la tarea principal del agente
        """
        pass