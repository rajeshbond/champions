from fastapi import FastAPI,BackgroundTasks, Request
from chartink import trasferDataToGoogleSheet
from datetime import datetime, timedelta
import asyncio
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
import json







app = FastAPI()

@app.get('/')
async def st():
    return {"Message" : "Hello"}

@app.get('/start')
async def start(background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(trasferDataToGoogleSheet)
    except Exception as e:
        print(f"Exception ----> {e}")
    return{"Message" : 'code run started'}


    



