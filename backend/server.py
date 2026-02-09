# This is an Expo React Native project, not a FastAPI project
# The actual backend is in /app/server/_core/index.ts (Node.js/Express)
# This file is a placeholder for the Emergent platform
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Dragaan Pro Proxy")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"status": "proxy", "message": "See Node.js server on port 3000"}

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "python-proxy"}
