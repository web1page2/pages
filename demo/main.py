from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Big Factorial API",
    description="Calculate factorials of very large integers",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "Big Factorial API",
        "usage": "/factorial/{n}"
    }


@app.get("/factorial/{n}")
def factorial(n: int):
    if n < 0:
        raise HTTPException(
            status_code=400,
            detail="n must be a non-negative integer"
        )

    # Prevent unnecessarily huge calculations
    if n > 100000:
        raise HTTPException(
            status_code=400,
            detail="n is too large. Maximum allowed value is 100000."
        )

    result = 1

    for i in range(2, n + 1):
        result *= i

    return {
        "n": n,
        "factorial": str(result)
    }
