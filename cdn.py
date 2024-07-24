from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from pathlib import Path
import uvicorn

app = FastAPI()

# Serve static files from the 'images' directory
app.mount("/images", StaticFiles(directory="images"), name="images")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
