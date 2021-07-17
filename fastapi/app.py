# 1. Library imports
import uvicorn
from fastapi import FastAPI
from BankNotes import BankNote
import numpy as np
import pickle
import pandas as pd

# 2. Create the app object
app = FastAPI()
pickle_in = open("./artifacts/classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get("/")
def index():
    return {"message": "Hello, World"}


# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get("/{name}")
def get_name(name: str):
    return {"Welcome To Jacques's fastapi for ml template ": f"{name}"}


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post("/predict")
def predict_banknote(data: BankNote):  # BankNote inherits BaseModel
    data = data.dict()
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]
    #    print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if prediction[0] > 0.5:
        prediction = "Fake note"
    else:
        prediction = "Its a Bank note"
    return {"prediction": prediction}


# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == "__main__":
    # execute the following in the command-line:
    # uvicorn app:app --reload
    # First app is file name
    # Second app is the FastAPI object name
    uvicorn.run(app, host="127.0.0.1", port=8000)
