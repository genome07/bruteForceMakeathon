from typing import Union

from fastapi import FastAPI, File, UploadFile
import uuid

IMAGEDIR = "images/"
app = FastAPI()

@app.get("/")
def read_root():
     return { "Hello" : "World" }

@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()
    #save the file
    with open(f"{IMAGEDIR}{file.filename}","wb") as f:
        f.write(contents)
        return {"filename": file.filename}
