# src/api/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ..graph.workflow import restaurant_workflow, RestaurantInfo

app = FastAPI(title="Restaurant Info API")

class RestaurantRequest(BaseModel):
    restaurant_name: str
    location: str

class RestaurantResponse(BaseModel):
    restaurant_name: str
    google_maps_data: dict = None
    tripadvisor_data: dict = None
    website_data: dict = None
    aggregated_data: dict = None
    firebase_result: dict = None
    error: str = None

@app.post("/restaurant-info", response_model=RestaurantResponse)
async def get_restaurant_info(request: RestaurantRequest):
    """Get comprehensive information about a restaurant"""
    try:
        # Initialize workflow with restaurant name
        initial_state = {"restaurant_name": request.restaurant_name, "location": request.location}
        
        # Execute workflow
        result = await restaurant_workflow.ainvoke(initial_state)
        
        return RestaurantResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)