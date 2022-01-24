from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router


def get_application():
    app_engine = FastAPI(title="Hedgehog Reservation", version="1.0.0")

    app_engine.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app_engine.include_router(api_router, prefix="/api")

    return app_engine


app = get_application()
