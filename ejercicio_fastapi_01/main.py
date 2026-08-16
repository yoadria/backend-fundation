import uvicorn
from fastapi import FastAPI, HTTPException
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/health")
async def health():
    return {"status":"ok"}

@app.post("/v1/turn")
async def turn(payload: dict):
    try:
        if not "user_id" in payload:
            return {"status":400,"error": "falta user id"}
        
        if not "message" in payload  or payload.get("message").strip(" ") == "":
            return {"status":400, "error": "falta message"}
        return {"status":200}
    except HTTPException as error:
        logger.error(f"[ERROR] -> {error} ")
        raise {"status": 401, "error": error}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=9000,
        log_level="info"
    )