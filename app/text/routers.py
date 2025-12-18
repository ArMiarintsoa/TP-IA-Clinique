from fastapi import APIRouter
from .service import TextService

router = APIRouter(prefix="/text", tags=["text"])

@router.get("/analyze")
def analyze_text(text: str):
    csv_file = "../teny_malagasy.csv"
    closest_word, distance = TextService.find_closest_word(text, csv_file)
    print(f"Mot le plus proche : {closest_word}, Distance : {distance}")
    return { "closest_word": closest_word }