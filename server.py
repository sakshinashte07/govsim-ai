# server.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Create app
app = FastAPI(title="My Hugging Face API")

# Allow CORS for all origins (so frontend can access API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Example data model for POST requests
class InputData(BaseModel):
    text: str

# Root route
@app.get("/")
def read_root():
    return {"message": "Server is running!"}

# Example POST endpoint
@app.post("/process")
def process_data(data: InputData):
    # Replace below with your processing logic
    result = data.text.upper()  # Example: convert text to uppercase
    return {"input": data.text, "output": result}

# Another example GET endpoint
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
