from fastapi import APIRouter

import requests
import os
import json

router = APIRouter()

@router.get("/")
async def get_voices():
    headers = {"accept": "application/json", "AUTHORIZATION": os.getenv("PLAY_HT_SECRET_KEY"), "X-USER-ID": os.getenv("PLAY_HT_USER_ID")}
    response = requests.get("https://play.ht/api/v2/voices", headers=headers)
    voices = json.loads(response.text)
    en_voices = [voice for voice in voices if voice["language_code"] == "en-US"]
    print(en_voices)
    return {"voices": en_voices}

