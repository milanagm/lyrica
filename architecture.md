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

#### Components:
- **React Application**
  - Built with Create React App
  - Uses modern React (v18.3.1)
  - Includes testing libraries and web vitals

#### Dependencies:
- React and React DOM
- Testing libraries (Jest, React Testing Library)
- Web Vitals for performance monitoring
- Concurrently for running multiple scripts

#### Scripts:
- `npm start`: Starts the development server
- `npm build`: Creates production build
- `npm test`: Runs test suite
- `npm eject`: Ejects from Create React App
- `npm backend`: Starts the backend server
- `npm dev`: Runs both frontend and backend concurrently




### 3. HTML Interface (`index.html`)

#### Components:
- Simple HTML interface for text file uploads
- Styled with CSS for modern look and feel
- JavaScript for file handling and display

#### Features:
- File upload functionality
- Text file validation
- Real-time text display
- Responsive design
- Custom styling with purple theme




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

2. **Testing**:
   - Frontend includes Jest and React Testing Library
   - Backend can be tested using FastAPI's testing tools
   - End-to-end testing possible through the complete stack

3. **Deployment**:
   - Frontend can be built for production using `npm run build`
   - Backend can be deployed using standard Python deployment methods
   - Environment variables need to be configured in production





