# Birthday App API

A minimal FastAPI backend with various endpoints.

## APIs

- `GET /random-number`: Returns a random number
- `GET /years?birthdate=YYYY-MM-DD`: Calculates years lived based on birthdate
- `GET /health`: Health check endpoint
- `GET /env`: Returns all environment variables

## Running Locally

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
uvicorn main:app --reload
```

## Running with Docker

1. Build the Docker image:
```bash
docker build -t birthday-app .
```

2. Run the container:
```bash
docker run -p 8000:8000 birthday-app
```

## API Documentation

Once the server is running, you can access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 