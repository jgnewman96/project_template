"""
Simple HTTP server to interact with python backend
"""

import logging

from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

LOGGER = logging.getLogger(__name__)
app = FastAPI()


origins = [
    "http://localhost:8800",
    "https://localhost:8800",
    "http://localhost:8100",
    "https://localhost:8100",
    "http://localhost",
    "http://localhost:3000",
    "https://localhost:3000",
    "http://172.21.0.2:8800",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/do")
def do() -> str:
    return "do"
