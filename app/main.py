from fastapi import FastAPI

from .routers import routers as credit_card

app = FastAPI()


app.include_router(
    credit_card.router,
    prefix="/validate",
    tags=['Validate Credit Cards']
)
