#!/usr/bin/env python3

from datetime import datetime

from fastapi import FastAPI
from uvicorn import run

app = FastAPI()

@app.get('/test')
async def test():
    return {'success': True, 'timestamp': datetime.now()

if __name__ == '__main__':
    run(app)
