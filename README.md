# FastAPI Mock Server with Jinja2 Templating

This is a simple **Mock Server** built using **FastAPI** that allows the user to create and query mock APIs with dynamic, customizable responses. The server uses **Jinja2** templating for generating flexible and dynamic responses based on provided query parameters.

## Features
- **Create Custom Mock APIs**: Define new APIs with custom response templates.
- **Dynamic Responses**: Use query parameters to dynamically modify the response based on the provided template.
- **JSON Responses**: The server generates responses in JSON format, making it easy to integrate with various applications.
- **RESTful API**: Supports GET and POST methods for interacting with mock APIs.

## Installation

To run the mock server, make sure you have **Python 3.7+** installed. Then, install the required dependencies by running:

```bash
pip install fastapi[all] jinja2 uvicorn
```

## Running the Server

To start the server, use Uvicorn:

```bash
uvicorn main:app --reload
```
This will run the server locally at http://127.0.0.1:8000.

## Usage

### 1. Get a Mock API Response

To query a mock API, send a GET request to /mock/{api_name} where {api_name} is the name of the mock API. Optionally, pass query parameters to customize the response.

Example Request:

```http
GET http://127.0.0.1:8000/mock/api/user?user_id=123&name=John
```
Example Response:

```json
{
    "user_id": "123",
    "name": "John"
}
```

### 2. Create a New Mock API

To create a new mock API, send a POST request to /mock/{api_name} with the name of the API and the details (method and response template).

Example Request:

```http
POST http://127.0.0.1:8000/mock/api/employee
Content-Type: application/json

{
    "method": "GET",
    "response_template": "{\"id\": \"{{ id }}\", \"role\": \"{{ role }}\"}"
}
```
Example Response:

```json
{
    "message": "API created successfully",
    "api_name": "api/employee"
}
```

### 3. Error Handling

If you try to query an undefined API, you'll get a 404 error:

```json
{
    "detail": "API not found"
}
```
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Feel free to open issues or pull requests for any improvements or features you'd like to add!
