from fastapi import FastAPI, HTTPException
from db import search_names
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/names")
def get_names(
    gender: str = "",
    letters: int | None = None,
    search_letter: str = ""
):
    gender = gender.strip().lower()
    search_letter = search_letter.strip()

    # التحقق من الجنس
    if gender and gender not in ("male", "female"):
        raise HTTPException(
            status_code=400,
            detail="Gender must be male or female"
        )

    # التحقق من عدد الحروف
    if letters is not None and letters <= 0:
        raise HTTPException(
            status_code=400,
            detail="Letters must be greater than zero"
        )

    # التحقق من حرف البحث
    arabic_letters = "ءآأؤإئابتثجحخدذرزسشصضطظعغفقكلمنهويىة"

    if search_letter:
        if len(search_letter) != 1 or search_letter not in arabic_letters:
            raise HTTPException(
                status_code=400,
                detail="Enter one Arabic letter"
            )

    results = search_names(gender, letters, search_letter)

    return {
        "count": len(results),
        "names": results
    }
