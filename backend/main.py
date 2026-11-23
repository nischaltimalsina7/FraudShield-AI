
# Import FastAPI to create our backend application.
from fastapi import FastAPI
# Import transaction schema
from backend.schemas import TransactionInput

# Create an application named "app".
# Uvicorn will look for this variable.
app = FastAPI(title="FraudShield AI")



# Run the home function when someone visits "/".
@app.get("/")
def home():

    # Return a welcome message in JSON format.
    return {
        "message": "Welcome to FraudShield AI",
        "status": "running"
    }


# Check whether our backend is working.
@app.get("/health")
def health():

    # Return the health status.
    return {
        "status": "healthy"
    }


# Receive and validate transaction data
@app.post("/predict")
def predict_transaction(transaction: TransactionInput):
    {
  "amount": 250.50,
  "merchant_category": "electronics",
  "transaction_hour": 22,
  "card_type": "debit"
}

    # Return received data (ML model not connected yet)
    return {
        "message": "Transaction received successfully",
        "transaction": transaction.model_dump(),
        "fraud_probability": None,
        "anomaly_score": None,
        "decision": "MODEL_NOT_CONNECTED"
    }
