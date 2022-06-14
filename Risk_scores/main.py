from random import randint
from fastapi import FastAPI

app = FastAPI() 

@app.get("/")
# An asynchronous method starts a job in the background 
# and returns to the caller immediately.
async def root():
    # cust_id, risk_score [1-100]
    risk_data = [
        {'cust_id': randint(1,9999), "risk_score": randint(1,100)}
        for _ in range(1000)
    ]
    return risk_data
