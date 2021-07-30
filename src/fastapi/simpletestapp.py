# This file is a simple test of FastAPI.

# 1. Library imports
import uvicorn  ##ASGI
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get("/")
def index():
    return {"message": "Hello, World"}


# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get("/Welcome")
def get_name(name: str):
    return {"Welcome to JayThibs FastAPI app": f"{name}"}


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
#    Test out application with Swagger docs at:
#    http://127.0.0.1:8000/docs
if __name__ == "__main__":
    # execute the following in the command-line:
    # uvicorn main:app --reload
    uvicorn.run(app, host="127.0.0.1", port=8000)
