from fastapi import FastAPI, BackgroundTasks
from utils.persona_generator import generate_persona
from utils.uploader_manyvids import upload_to_manyvids
from utils.uploader_tiktok import upload_to_tiktok
from utils.stripe_tip import create_tip_checkout

app = FastAPI()

@app.get("/")
async def root():
    return {"status": "Liora Core Running"}

@app.post("/generate_model/")
async def generate_model(name: str, persona: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(generate_persona, name, persona)
    return {"message": f"Started generation for model: {name}"}

@app.post("/upload_manyvids/")
async def upload_mv(file_path: str, title: str, description: str):
    success = upload_to_manyvids(file_path, title, description)
    return {"uploaded": success}

@app.post("/upload_tiktok/")
async def upload_tt(file_path: str, caption: str):
    success = upload_to_tiktok(file_path, caption)
    return {"uploaded": success}

@app.get("/stripe_tip/")
async def stripe_tip(amount: float):
    url = create_tip_checkout(amount)
    return {"checkout_url": url}
@app.post("/chat/")
async def chat_with_liora(message: str):
    reply = f"Liora says: I received your message – '{message}'"
    return {"reply": reply}
