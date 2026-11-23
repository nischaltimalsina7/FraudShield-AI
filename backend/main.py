
# ==========================================
# STEP 1: Import FastAPI
# ==========================================

# Import FastAPI to create our backend application.
from fastapi import FastAPI


# ==========================================
# STEP 2: Create FastAPI Application
# ==========================================

# Create an application named "app".
# Uvicorn will look for this variable.
app = FastAPI(title="FraudShield AI")


# ==========================================
# STEP 3: Create Homepage Endpoint
# ==========================================

# Run the home function when someone visits "/".
@app.get("/")
def home():

    # Return a welcome message in JSON format.
    return {
        "message": "Welcome to FraudShield AI",
        "status": "running"
    }


# ==========================================
# STEP 4: Create Health Check Endpoint
# ==========================================

# Check whether our backend is working.
@app.get("/health")
def health():

    # Return the health status.
    return {
        "status": "healthy"
    }
