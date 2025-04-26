from fastapi import FastAPI, Query, HTTPException
from patterns import patterns
from core import count_numbers_with_89

app = FastAPI(
    title="Ogathon Challenges API",
    version="1.0.0",
    description="Challenges para el Ogathon 3.0",
    docs_url="/swagger", 
)

@app.get("/challenges/solution-1")
def solution_1(n: int = Query(..., ge=0, description="Distancia objetivo")):
    """
    Devuelve el nº de patrones distintos para una distancia `n`.
    """
    return str(patterns(n))

@app.get("/challenges/solution-2", summary="Cuenta números que terminan en 89")
def solution_2(n: int = Query(..., gt=0, le=10_000_000)):
    """
    Devuelve cuántos enteros 1 ≤ k ≤ *`n`* generan una cadena que termina en **89**.
    """
    try:
        result = count_numbers_with_89(n)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
    return str(result)