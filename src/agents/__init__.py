# src/agents/__init__.py
"""
Módulo de agentes especializados.

Este módulo contiene los diferentes agentes que realizan tareas específicas
en el proceso de recopilación y estructuración de información de restaurantes.
"""

from .google_maps_chat_agent import GoogleMapsChatAgent

__all__ = [
    "GoogleMapsChatAgent"
]