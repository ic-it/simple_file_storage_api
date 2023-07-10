import os
import uvicorn

from .routers import file
from fastapi import FastAPI
from simple_file_storage_api.config import service_config

app = FastAPI()
app.include_router(file.file_router)

if not os.path.exists(service_config.storage_path):
    os.makedirs(service_config.storage_path)


def run() -> None:
    uvicorn.run(app, host=service_config.host, port=service_config.port)


if __name__ == "__main__":
    run()
