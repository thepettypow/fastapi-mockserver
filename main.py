from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from jinja2 import Template
from typing import Dict, Optional
import json

# Initialize FastAPI app
app = FastAPI()

# In-memory dictionary to store mock API definitions
mock_apis = {
    "/api/user": {
        "method": "GET",
        "response_template": '{"user_id": "{{ user_id }}", "name": "{{ name }}"}'
    }
}

# Function to retrieve mock API response based on query parameters
@app.get("/mock/{api_name}", response_class=JSONResponse)
async def mock_api(api_name: str, query_params: Optional[Dict[str, str]] = None):
    """
    Endpoint to serve mock API responses based on the stored templates.
    Supports dynamic response generation using Jinja2 templating engine.

    Args:
        api_name (str): The name of the mock API.
        query_params (Dict[str, str], optional): The query parameters used in the response template.

    Returns:
        JSONResponse: The dynamically generated mock response.
    """
    # Check if the requested API exists in mock_apis
    if api_name not in mock_apis:
        raise HTTPException(status_code=404, detail="API not found")

    # Get the mock API details
    api_info = mock_apis[api_name]

    # Render the response template with the provided query parameters
    template = Template(api_info["response_template"])
    response_content = template.render(query_params)

    # Return the rendered response as JSON
    return JSONResponse(content=json.loads(response_content))

# Endpoint to create a new mock API with a custom response template
@app.post("/mock/{api_name}")
async def create_mock_api(api_name: str, api_details: Dict[str, str]):
    """
    Endpoint to create a new mock API with a customizable response template.

    Args:
        api_name (str): The name of the new mock API.
        api_details (Dict[str, str]): The details of the mock API, including method and response template.

    Returns:
        dict: A confirmation message indicating success.
    """
    # Add the new mock API to the mock_apis dictionary
    mock_apis[api_name] = api_details
    return {"message": "API created successfully", "api_name": api_name}
