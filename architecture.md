# LyricAA - Architecture Documentation

## Overview
LyricAA is a full-stack application that analyzes emotions from text input and provides music recommendations based on the detected emotions. The application consists of three main components:
1. A FastAPI backend service for emotion classification
2. A React frontend application for user interaction
3. A simple HTML interface for text file uploads




## System Architecture

### 1. Backend Service (`/backend`)

#### Components:
- **main.py**: The core FastAPI application
  - Implements the `/classify` endpoint
  - Uses OpenAI's GPT-3.5-turbo model for emotion classification
  - Handles CORS middleware for cross-origin requests
  - Manages environment variables for API keys

- **models.py**: Data models
  - Defines the `TextInput` Pydantic model for request validation
  - Ensures type safety and data validation

- **requirements.txt**: Python dependencies
  - python-dotenv: Environment variable management
  - openai: OpenAI API integration
  - fastapi: Web framework
  - uvicorn[standard]: ASGI server

- **start_backend.sh**: Shell script to start the backend server
  - Launches the FastAPI application using uvicorn

#### API Endpoints: -> this is in main.py
- `POST /classify`
  - Input: JSON with `text` field
  - Output: JSON with `emotion` field
  - Function: Classifies emotions from input text using OpenAI's GPT model




### 2. Frontend Application (`/emotion-music-player`)
most important stuff:
- **public/index.html**:
    - includes the static styling 

- **src/App.css and index.css**: styling 

- **src/App.js** & **src/EmotionMusicPlayer.js**: 
    - calls OpenAI API and awaits response, defines window for response presentation




## Component Interactions

1. **Frontend to Backend Communication**:
   - Frontend sends text input to backend's `/classify` endpoint
   - Backend processes text using OpenAI API
   - Backend returns emotion classification
   - Frontend displays results to user

2. **HTML Interface to Backend**:
   - HTML interface allows text file uploads
   - Processes text content
   - Can potentially communicate with backend for emotion classification

3. **Environment Configuration**:
   - Backend uses `.env` file for API keys
   - Frontend configured for development and production environments
   - CORS enabled for cross-origin communication




## Development Workflow

1. **Local Development**:
   - Run `npm run dev` to start both frontend and backend (first cd into frontend)
   - Frontend runs on default React port (3000)
   - Backend runs on uvicorn server
   - HTML interface can be served separately




