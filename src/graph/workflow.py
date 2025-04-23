# src/graph/workflow.py
from typing import Dict, Any, TypedDict
from langgraph.graph import StateGraph, END
from src.agents import GoogleMapsChatAgent

class RestaurantInfo(TypedDict):
    restaurant_name: str
    location: str
    google_maps_data: Dict[str, Any]
    error: str

def create_restaurant_workflow():
    google_maps_agent = GoogleMapsChatAgent()
    # Define states
    workflow = StateGraph(RestaurantInfo)
    
    # Add nodes
    workflow.add_node("search_google_maps", google_maps_agent.run)

    workflow.set_entry_point("search_google_maps")
    
    # Define parallelism for search nodes
    workflow.add_edge("search_google_maps", END)
    
    return workflow.compile()

# Create a workflow instance
restaurant_workflow = create_restaurant_workflow()