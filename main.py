from typing import Optional
from fastapi import FastAPI

import os
import sys
import requests

from constants import client_id, client_secret

app = FastAPI()

BASE_URL = "https://openapi.naver.com/v1/search/blog?query="


@app.get("/search")
def search(keyword: str = "", display: int = 10, start: int = 1):
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }
    res = requests.get(url=f"{BASE_URL}{keyword}&display={display}&start={start}", headers=headers)
    json = res.json()

    return {"result": json}
