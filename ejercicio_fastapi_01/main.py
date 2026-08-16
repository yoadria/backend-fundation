import uvicorn
from fastapi import FastAPI
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/v1/turn")
def turn(payload: dict):
    if "user_id" not in payload:
        return {"status":400,"error": "falta user id"}
    
    if "message" not in payload  or payload.get("message").strip(" ") == "":
        return {"status":400, "error": "falta message"}
    
    response = {
        "received": True,
        "user": {
            "id": payload.get("user_id"),
            "name": payload.get("user_name")
        },
        "message": {
            "text": payload.get("message"),
            "length": len(payload.get("message"))
        },
        "companies_count": len(payload.get("allowed_company_ids"))
    }

    return response

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=9000,
        log_level="info"
    )