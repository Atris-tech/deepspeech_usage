from fastapi import FastAPI, File, UploadFile,HTTPException
from Transcribe.TranscribeHandler import TranscribeHandler
transcribeObj = TranscribeHandler()
app = FastAPI()

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    audio = await file.read()
    output = transcribeObj.transcribe(audio)
    print(output)
    if output["status"] == "error":
        raise HTTPException(status_code=400, detail="Bad Request")
    return output
