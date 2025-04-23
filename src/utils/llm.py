# src/utils/llm.py
import os
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain_tavily import TavilySearch

def get_llm():
    """
    Inicializa y devuelve el modelo OpenAI.
    """
    return ChatOpenAI(
        model_name="gpt-4o",
        temperature=0.2,
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )

class TavilyToolkit:
    """
    Adaptador que envuelve TavilySearch en una interfaz .get_tools()
    para LangChain React Agent.
    """
    def __init__(self):
        # Ajusta max_results y topic según tu caso
        self.tavily = TavilySearch(max_results=10, topic="general")

    def get_tools(self):
        """
        Devuelve una lista de langchain.tools.Tool
        con el método de búsqueda de Tavily.
        """
        return [
            Tool(
                name="tavily_search",
                func=self.tavily.search if hasattr(self.tavily, "search") else self.tavily.run,
                description="Búsqueda web general usando TavilySearch",
            )
        ]

def get_web_search_toolkit():
    """
    Inicializa y devuelve el toolkit para búsquedas web (TavilyToolkit).
    """
    return TavilyToolkit()