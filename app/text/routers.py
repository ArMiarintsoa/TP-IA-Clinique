from fastapi import APIRouter
from .service import TextService

router = APIRouter(prefix="/text", tags=["text"])

@router.get("/analyze")
def analyse_text(text: str):
    lev = TextService().levenshtein_distance(text, "textam")
    return { "message": lev }