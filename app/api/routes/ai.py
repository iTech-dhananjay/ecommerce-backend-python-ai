from fastapi import APIRouter, Depends, File, UploadFile
from app.core.security import require_role
from openai import OpenAI
import tempfile

router = APIRouter()

openai_client = OpenAI(api_key=settings.OPENAI_API_KEY)

@router.post("/generate-text")
def generate_text(prompt: str, user: dict = Depends(require_role(["admin", "superadmin"]))):
    response = openai_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"result": response.choices[0].message.content.strip()}

@router.post("/voice-to-text")
def voice_to_text(file: UploadFile = File(...), user: dict = Depends(require_role(["admin", "superadmin"]))):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(file.file.read())
        tmp_path = tmp.name
    transcript = openai_client.audio.transcriptions.create(
        model="whisper-1",
        file=open(tmp_path, "rb")
    )
    return {"result": transcript.text.strip()}

@router.post("/image-caption")
def image_caption(image: UploadFile = File(...), user: dict = Depends(require_role(["superadmin"]))):
    return {"result": "Image captioning is not yet implemented."}