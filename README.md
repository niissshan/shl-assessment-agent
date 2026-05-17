# SHL Assessment Recommendation Agent

This project is an AI-powered SHL assessment recommendation system.

## Features

- SHL catalog scraping
- Vector search using FAISS
- FastAPI backend
- Chat recommendation API
- Swagger API testing

## API Endpoints

### Health Check

GET /health

### Chat Endpoint

POST /chat

Example request:

```json
{
  "messages": [
    {
      "role": "user",
      "content": "I am hiring a Java developer"
    }
  ]
}

## Run Project

### Install dependencies

```bash
pip install -r requirements.txt

## Run server
cd app
uvicorn main:app --reload

## Open Swagger Docs

http://127.0.0.1:8000/docs