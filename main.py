from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from config import settings
from routers import voices, chatbot

load_dotenv()

app = FastAPI()

origins = [settings.CLIENT_ORIGIN]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(voices.router, prefix="/api/voices")
app.include_router(chatbot.router, prefix="/api/chatbots")

@app.get("/")
async def health_checker():
    return {"status": "success"}
