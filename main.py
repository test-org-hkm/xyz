from fastapi import FastAPI
from datetime import datetime
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(title="Birthday App API")

@app.get("/")
async def root():
    return {
        "message": "Welcome to Birthday App API",
        "endpoints": {
            "/random-number": "Returns a random number",
            "/years": "Calculate years lived (requires birthdate parameter in YYYY-MM-DD format)",
            "/health": "Health check endpoint",
            "/env": "Returns all environment variables",
            "/himanshu-birthday": "Returns HIMANSHU_BIRTHDAY from .env file",
            "/pikachu": "Returns Pikachu value from environment variables of k8"
        }
    }

@app.get("/random-number")
async def get_random_number():
    return {"number": random.randint(1, 100)}

@app.get("/years")
async def calculate_years(birthdate: str):
    """
    Calculate years lived based on birthdate
    
    Parameters:
    - Birthdate: Date in YYYY-MM-DD format (e.g., 1990-01-01)
    
    Returns:
    - years_lived: Number of years lived
    """
    try:
        birth_date = datetime.strptime(birthdate, "%Y-%m-%d")
        today = datetime.now()
        years = today.year - birth_date.year
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            years -= 1
        return {"years_lived": years}
    except ValueError:
        return {"error": "Invalid date format. Please use YYYY-MM-DD"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/env")
async def get_env():
    return dict(os.environ)

@app.get("/himanshu-birthday")
async def get_himanshu_birthday():
    """
    Returns the HIMANSHU_BIRTHDAY value from the .env file
    """
    birthday = os.getenv("HIMANSHU_BIRTHDAY")
    if birthday:
        return {"himanshu_birthday": birthday}
    return {"error": "HIMANSHU_BIRTHDAY not found in .env file"}

@app.get("/pikachu")
async def get_pikachu():
    """
    Returns the Pikachu value from environment variables
    """
    pikachu_value = os.getenv("PIKACHU")
    if pikachu_value:
        return {"pikachu": pikachu_value}
    return {"error": "Pikachu not found in environment variables"} 