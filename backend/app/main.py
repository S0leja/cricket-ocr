from fastapi import FastAPI

app = FastAPI()  # <- This must exist and be named exactly "app"

@app.get("/")
def root():
    return {"message": "Cricket OCR backend ready"}
