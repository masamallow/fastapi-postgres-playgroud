from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router as api_router
from app.core import config, tasks


def get_application() -> FastAPI:
    app_api = FastAPI(title=config.PROJECT_NAME, version=config.VERSION)

    app_api.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app_api.add_event_handler("startup", tasks.create_start_app_handler(app_api))
    app_api.add_event_handler("shutdown", tasks.create_stop_app_handler(app_api))

    app_api.include_router(api_router, prefix="/api")

    return app_api


# if __name__ == '__main__': 内で処理させた方が良いように思う (動作検証していない)
app = get_application()
