import asyncio
from datetime import datetime
from fastapi import FastAPI, HTTPException, Path
from starlette.responses import StreamingResponse
import httpx
from io import BytesIO
from codern import api
import logging

logger = logging.getLogger(__name__)

app = FastAPI()

async def download_audio(download_link: str) -> BytesIO:
    async with httpx.AsyncClient() as client:
        response = await client.get(download_link)
        response.raise_for_status()
        return BytesIO(response.content)

@app.get("/create_voice/{input_text}")
async def create_voice(input_text: str = Path(..., description="متن صدا")):
    try:
        download_link = api.create_voice(input_text)
        audio_stream = await download_audio(download_link)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"output_{timestamp}.mp3"

        return StreamingResponse(audio_stream, media_type="audio/mpeg", headers={"Content-Disposition": f"attachment; filename={filename}"})
    except Exception as e:
        logger.error(f"Error creating voice: {e}")
        raise HTTPException(status_code=500, detail="خطایی در تولید صدا رخ داده است.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)