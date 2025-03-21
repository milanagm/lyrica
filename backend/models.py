"""
models.py

This file contains the data models used for inputs in the FastAPI application.
- `TextInput`: Model for classifying emotions from a given text.

The goal is to keep the data structures clean and reusable.
"""
from pydantic import BaseModel

# Datenmodell für Eingaben
class TextInput(BaseModel):
    text: str
