from datetime import datetime
from io import BytesIO

from httpx import AsyncClient
from codern import api
from fastapi import FastAPI, HTTPException, Path
from starlette.responses import StreamingResponse

from utils import *  # Import utility functions and variables

app = FastAPI()  # Initialize FastAPI application

async def download_audio(download_link: str) -> BytesIO:
    """
    Downloads audio from the given link asynchronously and returns it as a BytesIO object.

    Args:
        download_link (str): The URL link to download the audio from.

    Returns:
        BytesIO: A BytesIO object containing the downloaded audio content.

    Raises:
        HTTPStatusError: If the HTTP request returned an unsuccessful status code.
    """
    async with AsyncClient() as client:
        response = await client.get(download_link)  # Perform asynchronous GET request
        response.raise_for_status()  # Raise an error if the request was unsuccessful
        return BytesIO(response.content)  # Return the audio content as a BytesIO object

@app.get("/create_voice/{input_text}")
async def create_voice(input_text: str = Path(..., description="Text for voice")):  # Description in English
    """
    Endpoint to create a voice from the given input text.

    Args:
        input_text (str): Text for voice.

    Returns:
        StreamingResponse: A streaming response with the generated audio file.

    Raises:
        HTTPException: If an error occurs while generating the voice.
    """
    try:
        download_link = api.create_voice(input_text)  # Call API to create voice and get download link
        audio_stream = await download_audio(download_link)  # Download the audio from the link

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Generate a timestamp for the filename
        filename = f"output_{timestamp}.mp3"  # Create a filename with the timestamp

        return StreamingResponse(audio_stream, media_type="audio/mpeg", headers={"Content-Disposition": f"attachment; filename={filename}"})  # Return the audio as a streaming response
    except Exception as e:
        logger.error(f"Error creating voice: {e}")  # Log the error
        raise HTTPException(status_code=500, detail="An error occurred while generating the voice.")  # Raise an HTTP exception with a 500 status code

if __name__ == "__main__":
    __import__("uvicorn").run(
        app, 
        host=settings.HOST, 
        port=settings.PORT
    )  # Run the FastAPI application using Uvicorn
