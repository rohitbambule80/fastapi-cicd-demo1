from fastapi import FastAPI
import random

app = FastAPI()

quotes = [
    "Success is not final, failure is not fatal.",
    "Stay hungry, stay foolish.",
    "Learning never exhausts the mind.",
    "Small progress is still progress."
]


@app.get("/")
def home():
    return {
        "message": "Quote API"
    }


@app.get("/quote")
def quote():
    return {
        "quote": random.choice(quotes)
    }
