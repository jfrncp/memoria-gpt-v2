{
  "openapi": "3.1.0",
  "info": {
    "title": "Memoria GPT",
    "version": "1.0.0"
  },
  "servers": [
    {
      "url": "https://memoria-gpt-v2.onrender.com"
    }
  ],
  "paths": {
    "/": {
      "get": {
        "summary": "Inicio",
        "operationId": "inicio_get",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    }
  }
}
