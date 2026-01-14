from fastapi import FastAPI

app = FastAPI(title="Talabat Iraq API")

@app.get("/health")
def health():
    return {"status": "ok"}
